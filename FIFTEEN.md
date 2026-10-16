# 15-Minute 1¢ Study

*Updated Fri Oct 16, 8:30 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1624 finished bets | 1% | $85.85 | +48% | +5.29¢ | $38.10 / $47.75 |

*Expect about **89 buys a day** (~$13.31/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1507 | $46.95 | +29% |
| Momentum model ≥ 2%, hold to the close | 2540 | -$0.30 | -0% |
| Volatility model ≥ 5%, sell at 50¢ | 1624 | -$16.65 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20859 | 20837 | 80 (0%) | 1.07% | -$1,416.65 (-56%) | Hold to the close: -$1,416.65 (-56%) |

*In play or awaiting result: 21. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 13321 | 4.4% | 0.4% (54) | -637% | ❌ Worse |
| Momentum model | 13321 | 4.4% | 0.4% (54) | -661% | ❌ Worse |
| Mean-reversion model | 13321 | 7.4% | 0.4% (54) | -766% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13321 | 54 | -49% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 2962 | 24 | -6% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1624 | 19 | +48% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 950 | 11 | +65% | -65% | -64% | -61% |
| Momentum model ≥ 2% | 2540 | 21 | -0% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1507 | 15 | +29% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1004 | 10 | +40% | -72% | -71% | -66% |
| Mean-reversion model ≥ 2% | 5008 | 34 | -26% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3447 | 27 | -14% | -82% | -81% | -77% |
| Mean-reversion model ≥ 10% | 2263 | 16 | -19% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13519 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5174 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2144 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20837 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 80 | 0% | -$1,416.65 | -56% | — |
| Sell at 2¢ | 742 | 4% | -$2,245.73 | -89% | 42 sec |
| Sell at 3¢ | 499 | 2% | -$2,244.04 | -88% | 47 sec |
| Sell at 5¢ | 361 | 2% | -$2,204.00 | -87% | 50 sec |
| Sell at 10¢ | 219 | 1% | -$2,123.76 | -84% | 63 sec |
| Sell at 25¢ | 126 | 1% | -$1,951.59 | -77% | 80 sec |
| Sell at 50¢ | 83 | 0% | -$1,738.40 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 683 | 5 | 10% | 3% | -30% | -82% | -86% |
| 2–5 min | 6758 | 37 | 7% | 3% | -46% | -88% | -87% |
| 1–2 min | 5424 | 20 | 3% | 2% | -60% | -92% | -92% |
| Under 1 min | 7968 | 18 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1517 | 11 | 5% | 3% | -10% | -89% | -89% |
| HYPE | 1514 | 5 | 4% | 2% | -59% | -90% | -89% |
| ETH | 1507 | 8 | 5% | 3% | -36% | -88% | -87% |
| DOGE | 1504 | 2 | 4% | 2% | -83% | -90% | -90% |
| BNB | 1504 | 6 | 5% | 2% | -51% | -90% | -90% |
| SOL | 1501 | 2 | 3% | 2% | -84% | -92% | -91% |
| XRP | 1494 | 7 | 2% | 1% | -42% | -86% | -87% |
| BTC | 1490 | 7 | 5% | 2% | -37% | -88% | -91% |
| NEAR | 1488 | 8 | 6% | 3% | -30% | -78% | -78% |
| GOLD | 846 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 820 | 4 | 3% | 1% | -44% | -79% | -79% |
| WTI | 788 | 3 | 3% | 1% | -56% | -94% | -95% |
| COPPER | 720 | 2 | 2% | 1% | -74% | -84% | -83% |
| PLATINUM | 704 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 649 | 2 | 1% | 0% | -71% | -84% | -84% |
| NATGAS | 647 | 5 | 2% | 2% | -28% | -82% | -80% |
| EURUSD | 641 | 3 | 3% | 1% | -56% | -81% | -81% |
| GBPUSD | 601 | 1 | 2% | 1% | -84% | -97% | -97% |
| USDJPY | 561 | 3 | 1% | 1% | -50% | -99% | -98% |
| AUDUSD | 183 | 0 | 1% | 0% | -100% | -99% | -99% |
| USDCAD | 158 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10502 | 40 | 4% | 2% | -56% | -89% | -89% |
| DOWN (bought NO) | 10335 | 40 | 4% | 2% | -55% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2237 | 11 | 2% | 1% | -17% | -79% | -79% |
| 0.05–0.1% | 2334 | 7 | 3% | 1% | -56% | -92% | -91% |
| 0.1–0.2% | 3427 | 11 | 4% | 2% | -60% | -90% | -90% |
| 0.2–0.5% | 3964 | 21 | 6% | 3% | -42% | -88% | -88% |
| Over 0.5% | 1554 | 6 | 7% | 3% | -60% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 4854 | 27 | 4% | 2% | -36% | -87% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,420 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 8:29:57 AM | ZEC | DOWN | 2 sec | -0.040% | 0¢ | In play | — |
| 10/16 8:29:57 AM | COPPER | DOWN | 2 sec | — | 0¢ | In play | — |
| 10/16 8:29:57 AM | EURUSD | DOWN | 2 sec | — | 0¢ | In play | — |
| 10/16 8:29:41 AM | USDJPY | UP | 18 sec | — | 0¢ | In play | — |
| 10/16 8:28:52 AM | USDCAD | UP | 67 sec | — | 0¢ | In play | — |
| 10/16 8:28:52 AM | SOL | DOWN | 67 sec | +0.238% | 0¢ | ❌ Lost | $0.00 |
| 10/16 8:28:52 AM | AUDUSD | DOWN | 67 sec | — | 0¢ | In play | — |
| 10/16 8:28:52 AM | DOGE | DOWN | 67 sec | +0.173% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:28:52 AM | HYPE | UP | 67 sec | -0.264% | 0¢ | ❌ Lost | $0.00 |
| 10/16 8:28:36 AM | PALLADIUM | DOWN | 83 sec | — | 0¢ | In play | — |
| 10/16 8:28:36 AM | GBPUSD | DOWN | 83 sec | — | 0¢ | In play | — |
| 10/16 8:28:36 AM | PLATINUM | DOWN | 83 sec | — | 0¢ | In play | — |
| 10/16 8:28:20 AM | WTI | UP | 1.6 min | — | 1¢ | In play | — |
| 10/16 8:27:47 AM | XRP | DOWN | 2.2 min | +0.232% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:27:31 AM | NEAR | DOWN | 2.5 min | +0.469% | 9¢ | ❌ Lost | -$0.15 |
| 10/16 8:27:15 AM | SILVER | DOWN | 2.7 min | — | 1¢ | In play | — |
| 10/16 8:26:42 AM | GOLD | DOWN | 3.3 min | — | 1¢ | In play | — |
| 10/16 8:26:26 AM | BTC | DOWN | 3.5 min | +0.285% | 1¢ | In play | — |
| 10/16 8:25:07 AM | ETH | DOWN | 4.9 min | +0.442% | 2¢ | In play | — |
| 10/16 8:24:36 AM | BNB | DOWN | 5.4 min | +0.223% | 1¢ | In play | — |
| 10/16 8:14:56 AM | USDJPY | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:14:56 AM | GBPUSD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:14:56 AM | GOLD | DOWN | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/16 8:14:40 AM | XRP | DOWN | 20 sec | +0.075% | 0¢ | ❌ Lost | $0.00 |
| 10/16 8:14:40 AM | NATGAS | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:14:09 AM | BTC | DOWN | 51 sec | +0.172% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:14:09 AM | EURUSD | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:14:09 AM | DOGE | DOWN | 51 sec | +0.218% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:14:09 AM | BNB | DOWN | 51 sec | +0.100% | 0¢ | ❌ Lost | $0.00 |
| 10/16 8:14:09 AM | PLATINUM | UP | 51 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
