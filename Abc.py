def generate_suggestions(rules, top_n=5):
    suggestions = []
    # Sort rules by confidence (primary), lift (secondary), and support (tertiary) in descending order
    sorted_rules = rules.sort_values(by=['confidence', 'lift', 'support'], ascending=[False, False, False])
    
    # Generate suggestions for the top N rules
    for _, rule in sorted_rules.head(top_n).iterrows():
        antecedents = rule['antecedents']
        consequents = rule['consequents']
        support = rule['support']
        antecedent_support = rule['antecedent support']
        consequent_support = rule['consequent support']
        confidence = rule['confidence']
        lift = rule['lift']
        leverage = rule['leverage']
        
        # Convert lift to percentage
        lift_percentage = (lift - 1) * 100
        
        # Generate a suggestion based on the rule
        if confidence > 0.8 and lift > 1.5 and support > 0.05:
            suggestions.append(
                f"💡 **Strong Association**: Customers who buy **{antecedents}** (Antecedent Support: {antecedent_support:.2f}) "
                f"are **{lift_percentage:.0f}%** more likely to buy **{consequents}** (Consequent Support: {consequent_support:.2f}). "
                f"(Support: {support:.2f}, Confidence: {confidence:.2f}, Leverage: {leverage:.3f}). "
                "Consider bundling these items or placing them close to each other."
            )
        elif confidence > 0.6 and lift > 1.2 and support > 0.03:
            suggestions.append(
                f"💡 **Moderate Association**: Customers who buy **{antecedents}** (Antecedent Support: {antecedent_support:.2f}) "
                f"are **{lift_percentage:.0f}%** more likely to buy **{consequents}** (Consequent Support: {consequent_support:.2f}). "
                f"(Support: {support:.2f}, Confidence: {confidence:.2f}, Leverage: {leverage:.3f}). "
                "This could be a potential cross-selling opportunity."
            )
        else:
            suggestions.append(
                f"💡 **Weak Association**: The relationship between **{antecedents}** (Antecedent Support: {antecedent_support:.2f}) "
                f"and **{consequents}** (Consequent Support: {consequent_support:.2f}) is not strong "
                f"(Support: {support:.2f}, Confidence: {confidence:.2f}, Leverage: {leverage:.3f}). "
                "Further analysis may be needed."
            )
    
    return "\n\n".join(suggestions)
