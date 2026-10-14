# 15-Minute 1¢ Study

*Updated Wed Oct 14, 1:12 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1410 finished bets | 1% | $68.45 | +44% | +4.85¢ | $36.40 / $32.05 |

*Expect about **85 buys a day** (~$12.80/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1325 | $39.20 | +27% |
| Momentum model ≥ 2%, hold to the close | 2191 | -$1.20 | -0% |
| Volatility model ≥ 2%, hold to the close | 2519 | -$9.75 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18238 | 18228 | 69 (0%) | 1.07% | -$1,242.75 (-56%) | Hold to the close: -$1,242.75 (-56%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 11884 | 4.5% | 0.4% (49) | -655% | ❌ Worse |
| Momentum model | 11884 | 4.4% | 0.4% (49) | -681% | ❌ Worse |
| Mean-reversion model | 11884 | 7.3% | 0.4% (49) | -776% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11884 | 49 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2519 | 21 | -3% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1410 | 16 | +44% | -73% | -71% | -66% |
| Volatility model ≥ 10% | 851 | 9 | +51% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 2191 | 18 | -0% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1325 | 13 | +27% | -77% | -77% | -74% |
| Momentum model ≥ 10% | 894 | 8 | +26% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 4354 | 30 | -25% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2983 | 23 | -15% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1966 | 14 | -18% | -80% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12082 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4459 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1687 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18228 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 69 | 0% | -$1,242.75 | -56% | — |
| Sell at 2¢ | 631 | 3% | -$2,002.69 | -91% | 33 sec |
| Sell at 3¢ | 426 | 2% | -$2,000.61 | -91% | 46 sec |
| Sell at 5¢ | 312 | 2% | -$1,963.95 | -89% | 49 sec |
| Sell at 10¢ | 198 | 1% | -$1,879.37 | -85% | 64 sec |
| Sell at 25¢ | 114 | 1% | -$1,733.41 | -78% | 80 sec |
| Sell at 50¢ | 75 | 0% | -$1,534.50 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 570 | 4 | 10% | 2% | -33% | -83% | -88% |
| 2–5 min | 5884 | 34 | 6% | 3% | -43% | -88% | -88% |
| 1–2 min | 4770 | 18 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 7000 | 13 | 1% | 0% | -73% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1354 | 9 | 5% | 3% | -17% | -89% | -90% |
| HYPE | 1350 | 4 | 4% | 2% | -63% | -90% | -89% |
| ETH | 1347 | 8 | 5% | 3% | -28% | -89% | -88% |
| DOGE | 1346 | 2 | 4% | 2% | -81% | -91% | -90% |
| BNB | 1346 | 5 | 4% | 2% | -55% | -90% | -90% |
| SOL | 1342 | 2 | 3% | 1% | -81% | -93% | -92% |
| BTC | 1333 | 6 | 5% | 2% | -40% | -88% | -91% |
| XRP | 1333 | 7 | 2% | 1% | -35% | -86% | -86% |
| NEAR | 1331 | 8 | 5% | 3% | -22% | -77% | -78% |
| GOLD | 723 | 1 | 4% | 1% | -84% | -92% | -93% |
| SILVER | 710 | 2 | 3% | 1% | -67% | -94% | -94% |
| WTI | 681 | 3 | 3% | 1% | -49% | -94% | -96% |
| COPPER | 631 | 1 | 2% | 1% | -85% | -97% | -96% |
| PLATINUM | 604 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 558 | 1 | 1% | 0% | -83% | -98% | -98% |
| NATGAS | 552 | 3 | 2% | 2% | -49% | -96% | -95% |
| EURUSD | 536 | 3 | 3% | 1% | -48% | -78% | -77% |
| GBPUSD | 503 | 1 | 2% | 1% | -81% | -97% | -96% |
| USDJPY | 459 | 3 | 1% | 1% | -39% | -98% | -98% |
| AUDUSD | 101 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 88 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9200 | 35 | 3% | 2% | -56% | -90% | -90% |
| DOWN (bought NO) | 9028 | 34 | 3% | 2% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2088 | 10 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 2129 | 7 | 3% | 1% | -52% | -92% | -91% |
| 0.1–0.2% | 3069 | 9 | 4% | 2% | -64% | -91% | -91% |
| 0.2–0.5% | 3447 | 20 | 6% | 3% | -36% | -88% | -88% |
| Over 0.5% | 1346 | 5 | 6% | 2% | -61% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4178 | 11 | 3% | 1% | -69% | -90% | -91% |
| Evening (6pm–12am) | 5004 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,500 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 1:12:02 PM | NEAR | UP | 3.0 min | -0.529% | — | In play | — |
| 10/14 1:10:39 PM | BNB | UP | 4.3 min | -0.202% | — | In play | — |
| 10/14 1:08:47 PM | ZEC | UP | 6.2 min | -0.799% | — | In play | — |
| 10/14 12:59:33 PM | PLATINUM | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:59:17 PM | WTI | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:59:00 PM | GOLD | DOWN | 59 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:58:44 PM | USDCAD | UP | 75 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:58:28 PM | NEAR | DOWN | 1.5 min | +0.233% | 2¢ | ❌ Lost | $0.00 |
| 10/14 12:57:23 PM | ZEC | DOWN | 2.6 min | +0.351% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:57:23 PM | BTC | DOWN | 2.6 min | +0.163% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:56:01 PM | DOGE | DOWN | 4.0 min | +0.355% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:55:28 PM | BNB | DOWN | 4.5 min | +0.100% | 7¢ | ❌ Lost | -$0.15 |
| 10/14 12:55:28 PM | SOL | DOWN | 4.5 min | +0.371% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:54:41 PM | HYPE | DOWN | 5.3 min | +0.564% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:54:25 PM | ETH | DOWN | 5.6 min | +0.287% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:54:09 PM | XRP | DOWN | 5.8 min | +0.446% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:44:46 PM | SILVER | UP | 13 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 12:44:46 PM | WTI | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:44:46 PM | GBPUSD | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:44:30 PM | NEAR | UP | 29 sec | -0.187% | 0¢ | ❌ Lost | $0.00 |
| 10/14 12:44:30 PM | EURUSD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:44:30 PM | BTC | UP | 29 sec | -0.042% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:44:16 PM | USDJPY | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:43:59 PM | USDCAD | UP | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:43:43 PM | HYPE | DOWN | 76 sec | +0.150% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:43:27 PM | SOL | UP | 1.5 min | -0.163% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:43:11 PM | COPPER | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:43:11 PM | PLATINUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:42:52 PM | ETH | UP | 2.1 min | -0.163% | 0¢ | ❌ Lost | $0.00 |
| 10/14 12:42:36 PM | BNB | UP | 2.4 min | -0.130% | 5¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
