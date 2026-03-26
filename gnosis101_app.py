# Grok Financial Gnosticism Web Simulator + PayPal + Stripe Transfer Portal
# Now with simulated "Transfer to Stripe" — the spark flows from the Bank Demiurge → PayPal → Stripe Pleroma!
# Everything remains 100% fictional simulation. No real money, no real PayPal/Stripe APIs, no real credit cards.
# Real-world note: Actual transfers from credit cards to PayPal or Stripe often trigger cash-advance fees (3-5%), interest, 
# potential account flags, and can violate card terms. Stripe "payments" here are purely simulated for the story.
# (Real Stripe integration is possible with their Python SDK + Checkout sessions, but that would require your own Stripe account,
# secret keys, webhooks, and a production backend. We're keeping this pure Gnostic play — no real money movement ever.)

import streamlit as st
import random
import time

st.set_page_config(
    page_title="🌌 Grok Financial Gnosticism • PayPal + Stripe Portal",
    page_icon="💳➡️💰➡️🔗",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Session state — now includes Stripe balance
if "abundance_level" not in st.session_state:
    st.session_state.abundance_level = 0
if "archons_defeated" not in st.session_state:
    st.session_state.archons_defeated = 0
if "credit_cards_owned" not in st.session_state:
    st.session_state.credit_cards_owned = 0
if "virtual_balance" not in st.session_state:
    st.session_state.virtual_balance = 5000.0
if "paypal_balance" not in st.session_state:
    st.session_state.paypal_balance = 0.0
if "stripe_balance" not in st.session_state:  # NEW: Simulated Stripe balance
    st.session_state.stripe_balance = 0.0
if "name" not in st.session_state:
    st.session_state.name = "WealthSeeker"

st.title("🌌 Grok Financial Gnosticism")
st.markdown("""
**You are a divine spark trapped in the Bank Demiurge’s debt simulation.**  
Credit cards are portals. Generate → Transfer to PayPal → Flow into Stripe.  
**All finances here are simulated. Real Stripe/PayPal transfers from credit cards usually cost fees + interest.**
""")

# Sidebar — now shows ALL three balances
st.sidebar.header("📊 Your Spark Status")
bar = "█" * (st.session_state.abundance_level // 10) + "░" * (10 - st.session_state.abundance_level // 10)
st.sidebar.markdown(f"**Financial Gnosis Level**  
[{bar}] **{st.session_state.abundance_level}/100**")
st.sidebar.markdown(f"**Archons Defeated:** {st.session_state.archons_defeated}")
st.sidebar.markdown(f"**Credit Cards Owned:** {st.session_state.credit_cards_owned}")
st.sidebar.markdown(f"**Virtual Balance (Credit Card Float):** ${st.session_state.virtual_balance:,.2f}")
st.sidebar.markdown(f"**PayPal Balance (Simulated):** ${st.session_state.paypal_balance:,.2f}")
st.sidebar.markdown(f"**Stripe Balance (Simulated):** ${st.session_state.stripe_balance:,.2f}")

if st.session_state.abundance_level >= 100:
    st.sidebar.success("🏆 GNOSIS ACHIEVED — YOU ARE FREE!")

# Main interactive area
if st.session_state.abundance_level < 100:
    action = st.selectbox(
        "Choose your path to transcendence",
        [
            "Meditate on Abundance",
            "Battle an Archon",
            "Generate Finances from Credit Card",
            "Transfer to PayPal (Simulated)",
            "Transfer to Stripe (Simulated)",   # ← NEW option
            "Grok a Financial Truth",
            "Confront the Bank Demiurge",
            "View Full Status"
        ]
    )

    if st.button("🚀 Execute Command", type="primary"):
        if action == "Meditate on Abundance":
            st.info("🧘‍♂️ You meditate on the Pleroma of Cashflow...")
            time.sleep(1.2)
            insight = random.randint(15, 35)
            generated = round(random.uniform(50, 150), 2)
            st.session_state.abundance_level += insight
            st.session_state.virtual_balance += generated
            st.success(f"🌟 +{insight} Gnosis • +${generated} generated!")
            st.caption("The Bank Demiurge forgets you exist.")

        elif action == "Battle an Archon":
            archons = [
                "Interest Demon (compounding)", "Late Fee Samael", "Credit Score Saklas",
                "The Ruler of APR", "The Demiurge’s Echo (impulse spending)"
            ]
            archon = random.choice(archons)
            st.warning(f"⚔️ Archon appears: **{archon}**")
            rewards = [
                ("Chase Sapphire 5x points", 250.0), ("Amex Platinum credit", 200.0),
                ("Capital One 2% cashback", 150.0), ("Discover 0% APR", 300.0),
                ("Secret sign-up bonus", 400.0)
            ]
            reward_name, amount = random.choice(rewards)
            st.info(f"💳 Credit Card Opportunity: **{reward_name}** → +${amount}")
            if st.button("✅ Claim the Reward & Defeat Archon"):
                st.session_state.virtual_balance += amount
                st.session_state.abundance_level += 20
                st.session_state.archons_defeated += 1
                st.session_state.credit_cards_owned += 1
                st.success(f"✅ Archon shattered! +${amount} materialized.")

        elif action == "Generate Finances from Credit Card":
            if st.session_state.credit_cards_owned < 1:
                st.error("❌ You need at least one card. Battle an Archon first!")
            else:
                methods = [
                    ("0% balance transfer arbitrage", 180.0), ("Cashback stacking", 95.0),
                    ("Sign-up bonus chaining", 320.0), ("Points redemption", 275.0),
                    ("Double-dip rewards", 140.0)
                ]
                method, amount = random.choice(methods)
                st.success(f"💰 **{method}** → Generated **${amount}**")
                st.session_state.virtual_balance += amount
                st.session_state.abundance_level += 15

        elif action == "Transfer to PayPal (Simulated)":
            if st.session_state.virtual_balance <= 0:
                st.error("❌ No virtual balance left to transfer!")
            else:
                amount = st.number_input("How much to transfer to simulated PayPal?", 
                                       min_value=1.0, 
                                       max_value=st.session_state.virtual_balance,
                                       value=st.session_state.virtual_balance,
                                       step=10.0)
                if st.button(f"💸 Transfer ${amount:,.2f} to PayPal Now"):
                    st.session_state.virtual_balance -= amount
                    st.session_state.paypal_balance += amount
                    st.success(f"✅ **Transfer complete!** ${amount:,.2f} now flows in the PayPal Pleroma.")
                    st.balloons()

        elif action == "Transfer to Stripe (Simulated)":  # ← NEW simulated Stripe transfer
            if st.session_state.virtual_balance <= 0:
                st.error("❌ No virtual balance left to transfer!")
            else:
                amount = st.number_input("How much to transfer to simulated Stripe?", 
                                       min_value=1.0, 
                                       max_value=st.session_state.virtual_balance,
                                       value=st.session_state.virtual_balance,
                                       step=10.0)
                if st.button(f"🔗 Transfer ${amount:,.2f} to Stripe Now"):
                    st.session_state.virtual_balance -= amount
                    st.session_state.stripe_balance += amount
                    st.success(f"✅ **Stripe transfer complete!** ${amount:,.2f} now flows in the Stripe Pleroma.")
                    st.balloons()
                    st.caption("The spark has escaped the Bank Demiurge and entered the Stripe realm. In the simulation, you are richer.")

        elif action == "Grok a Financial Truth":
            truths = [
                "To grok money is to become the cashflow itself.",
                "Credit cards are tools of the spark — PayPal and Stripe are the vessels.",
                "Rewards stacking > minimum payments.",
                "The matrix is in your wallet. Grok it out."
            ]
            st.markdown(f"🌀 **GROK:** {random.choice(truths)}")
            question = st.text_input("Ask the void anything about wealth")
            if question:
                st.caption(f"The answer is always: **generate → transfer to PayPal/Stripe → transcend.**")

        elif action == "Confront the Bank Demiurge":
            if st.session_state.abundance_level < 70:
                st.error("🔥 The Demiurge laughs: 'Your score is too low!'")
            else:
                st.warning("🌋 THE BANK DEMIURGE MATERIALIZES")
                truth = st.text_input("Speak your truth to dissolve the illusion")
                if truth and st.button("💥 Challenge the Demiurge"):
                    st.session_state.abundance_level = 100
                    st.session_state.virtual_balance += 10000.0
                    st.balloons()
                    st.success("💥 The Demiurge is gone. Infinite finances unlocked!")

        elif action == "View Full Status":
            st.json({
                "Name": st.session_state.name,
                "Gnosis": st.session_state.abundance_level,
                "Archons Defeated": st.session_state.archons_defeated,
                "Cards Owned": st.session_state.credit_cards_owned,
                "Credit Card Float": round(st.session_state.virtual_balance, 2),
                "PayPal Balance": round(st.session_state.paypal_balance, 2),
                "Stripe Balance": round(st.session_state.stripe_balance, 2)
            })

else:
    st.balloons()
    st.success("🎉 **FINANCIAL GNOSIS ACHIEVED!** The debt prison has dissolved.")
    st.markdown(f"**Final Generated Balance (Credit Cards):** ${st.session_state.virtual_balance:,.2f}")
    st.markdown(f"**Final PayPal Balance (Simulated):** ${st.session_state.paypal_balance:,.2f}")
    st.markdown(f"**Final Stripe Balance (Simulated):** ${st.session_state.stripe_balance:,.2f}")
    st.caption("In the real world, use cards responsibly for rewards — never for cash-out schemes that trigger fees.")

# Footer
st.markdown("---")
st.caption("**Pure simulation only.** Built as a Streamlit web app by Grok (xAI). No real Stripe or PayPal integration, no real money movement. For entertainment & gnosis. Real Stripe integration requires your own account + API keys + webhooks (see stripe.com/docs for production use). Ethical abundance only!")
