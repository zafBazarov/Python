import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import gradio as gr

# Function to clean frozenset strings and remove single quotes
def clean_frozenset(item):
    return str(item).replace("frozenset({", "").replace("})", "").replace("'", "").strip()

# Function to read the uploaded file (CSV or Excel)
def read_file(file):
    if file.name.endswith('.csv'):
        return pd.read_csv(file)
    elif file.name.endswith('.xlsx') or file.name.endswith('.xls'):
        return pd.read_excel(file)
    else:
        raise ValueError("Unsupported file format. Please upload a CSV or Excel file.")

# Function to generate top 5 or top 10 suggestions/comments based on association rules
def generate_suggestions(rules, top_n=5):
    suggestions = []
    # Sort rules by confidence (primary), lift (secondary), and support (tertiary) in descending order
    sorted_rules = rules.sort_values(by=['confidence', 'lift', 'support'], ascending=[False, False, False])
    
    # Generate suggestions for the top N rules
    for _, rule in sorted_rules.head(top_n).iterrows():
        antecedents = rule['antecedents']
        consequents = rule['consequents']
        support = rule['support']
        confidence = rule['confidence']
        lift = rule['lift']
        leverage = rule['leverage']
        
        # Convert lift to percentage
        lift_percentage = (lift - 1) * 100
        
        # Generate a suggestion based on the rule
        if confidence > 0.8 and lift > 1.5 and support > 0.05:
            suggestions.append(
                f"💡 **Strong Association**: Customers who buy **{antecedents}** are **{lift_percentage:.0f}%** more likely to buy **{consequents}** "
                f"(Support: {support:.2f}, Confidence: {confidence:.2f}, Leverage: {leverage:.3f}). "
                "Consider bundling these items or placing them close to each other."
            )
        elif confidence > 0.6 and lift > 1.2 and support > 0.03:
            suggestions.append(
                f"💡 **Moderate Association**: Customers who buy **{antecedents}** are **{lift_percentage:.0f}%** more likely to buy **{consequents}** "
                f"(Support: {support:.2f}, Confidence: {confidence:.2f}, Leverage: {leverage:.3f}). "
                "This could be a potential cross-selling opportunity."
            )
        else:
            suggestions.append(
                f"💡 **Weak Association**: The relationship between **{antecedents}** and **{consequents}** is not strong "
                f"(Support: {support:.2f}, Confidence: {confidence:.2f}, Leverage: {leverage:.3f}). "
                "Further analysis may be needed."
            )
    
    return "\n\n".join(suggestions)

# Function to process the file and generate association rules
def process_csv(file):
    # Read the file
    basket = read_file(file)
    
    # Remove null values
    basket = basket.dropna()
    
    # Grouping
    basket.Description = basket.Description.transform(lambda x: [x])
    basket = basket.groupby(['CustomerID', 'InvoiceDate']).sum()['Description'].reset_index(drop=True)
    
    # Encode transactions
    encoder = TransactionEncoder()
    transactions = pd.DataFrame(encoder.fit(basket).transform(basket), columns=encoder.columns_)
    
    # Generate frequent itemsets
    frequent_itemsets = apriori(transactions, min_support=6/len(basket), use_colnames=True, max_len=2, low_memory=True)
    
    # Generate association rules
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0, num_itemsets=len(frequent_itemsets))
    
    # Clean up frozenset strings in the 'antecedents' and 'consequents' columns
    rules['antecedents'] = rules['antecedents'].apply(clean_frozenset)
    rules['consequents'] = rules['consequents'].apply(clean_frozenset)
    
    # Sort rules by confidence, lift, and support
    sorted_rules = rules.sort_values(by=['confidence', 'lift', 'support'], ascending=[False, False, False])
    
    # Generate top 5 suggestions/comments
    suggestions = generate_suggestions(sorted_rules, top_n=5)
    
    # Return the sorted rules, a message, and suggestions
    return sorted_rules.head(), f"Rules identified: {len(rules)}", suggestions

# Function to save the results to a CSV file
def save_results(file):
    # Read the file
    basket = read_file(file)
    
    # Remove null values
    basket = basket.dropna()
    
    # Grouping
    basket.Description = basket.Description.transform(lambda x: [x])
    basket = basket.groupby(['CustomerID', 'InvoiceDate']).sum()['Description'].reset_index(drop=True)
    
    # Encode transactions
    encoder = TransactionEncoder()
    transactions = pd.DataFrame(encoder.fit(basket).transform(basket), columns=encoder.columns_)
    
    # Generate frequent itemsets
    frequent_itemsets = apriori(transactions, min_support=6/len(basket), use_colnames=True, max_len=2, low_memory=True)
    
    # Generate association rules
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0, num_itemsets=len(frequent_itemsets))
    
    # Clean up frozenset strings in the 'antecedents' and 'consequents' columns
    rules['antecedents'] = rules['antecedents'].apply(clean_frozenset)
    rules['consequents'] = rules['consequents'].apply(clean_frozenset)
    
    # Save the rules to a CSV file
    rules.to_csv("association_rules.csv", index=False)
    return "Results saved to 'association_rules.csv'."

# Gradio interface with three distinct sections
with gr.Blocks() as demo:
    gr.Markdown("## Market Basket Analysis")
    gr.Markdown("Upload a CSV or Excel file to generate association rules using the Apriori algorithm.")
    
    # Section 1: Upload Section
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Upload Section")
            file_input = gr.File(label="Upload CSV or Excel File")
            process_button = gr.Button("Process File")
    
    # Section 2: Result Section
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Result Section")
            output_table = gr.Dataframe(label="Top 5 Association Rules")
            output_message = gr.Textbox(label="Result")
            suggestions_box = gr.Textbox(label="Top 5 Suggestions/Comments", lines=10, interactive=False)
    
    # Section 3: Save Section
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Save Section")
            save_button = gr.Button("Save Results")
            save_message = gr.Textbox(label="Save Status", interactive=False)
    
    # Process file and display results when the "Process File" button is clicked
    process_button.click(process_csv, inputs=file_input, outputs=[output_table, output_message, suggestions_box])
    
    # Save results when the "Save Results" button is clicked
    save_button.click(save_results, inputs=file_input, outputs=save_message)

# Launch the app
demo.launch()
