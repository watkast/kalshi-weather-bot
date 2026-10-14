# 15-Minute 1¢ Study

*Updated Tue Oct 13, 7:10 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1305 finished bets | 1% | $38.90 | +27% | +2.98¢ | $27.95 / $10.95 |

*Expect about **83 buys a day** (~$12.41/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1242 | $20.35 | +15% |
| 5+ min left, hold to the close | 507 | -$18.55 | -25% |
| Volatility model ≥ 5%, sell at 50¢ | 1305 | -$20.10 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 17106 | 17096 | 65 (0%) | 1.07% | -$1,159.10 (-56%) | Hold to the close: -$1,159.10 (-56%) |

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
| Volatility model | 11262 | 4.4% | 0.4% (46) | -658% | ❌ Worse |
| Momentum model | 11262 | 4.4% | 0.4% (46) | -685% | ❌ Worse |
| Mean-reversion model | 11262 | 7.2% | 0.4% (46) | -773% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11262 | 46 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2329 | 18 | -10% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1305 | 13 | +27% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 800 | 9 | +61% | -64% | -63% | -60% |
| Momentum model ≥ 2% | 2041 | 15 | -11% | -80% | -80% | -78% |
| Momentum model ≥ 5% | 1242 | 11 | +15% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 845 | 8 | +34% | -70% | -69% | -65% |
| Mean-reversion model ≥ 2% | 4052 | 27 | -27% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2769 | 20 | -20% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 1824 | 14 | -11% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11460 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4129 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 1507 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 17096 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 65 | 0% | -$1,159.10 | -56% | — |
| Sell at 2¢ | 589 | 3% | -$1,873.96 | -91% | 33 sec |
| Sell at 3¢ | 392 | 2% | -$1,874.22 | -91% | 46 sec |
| Sell at 5¢ | 283 | 2% | -$1,843.15 | -89% | 48 sec |
| Sell at 10¢ | 180 | 1% | -$1,763.30 | -85% | 63 sec |
| Sell at 25¢ | 101 | 1% | -$1,636.79 | -79% | 77 sec |
| Sell at 50¢ | 65 | 0% | -$1,462.35 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 503 | 4 | 11% | 3% | -24% | -81% | -87% |
| 2–5 min | 5513 | 32 | 6% | 3% | -43% | -88% | -88% |
| 1–2 min | 4509 | 17 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 6567 | 12 | 1% | 0% | -73% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1286 | 7 | 4% | 2% | -32% | -90% | -90% |
| HYPE | 1281 | 4 | 4% | 2% | -61% | -90% | -89% |
| ETH | 1277 | 8 | 5% | 3% | -23% | -89% | -88% |
| BNB | 1277 | 5 | 4% | 1% | -52% | -91% | -91% |
| DOGE | 1276 | 2 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1272 | 2 | 3% | 1% | -80% | -93% | -92% |
| BTC | 1266 | 6 | 5% | 2% | -37% | -88% | -91% |
| XRP | 1263 | 7 | 2% | 1% | -31% | -85% | -86% |
| NEAR | 1262 | 7 | 5% | 2% | -27% | -77% | -78% |
| GOLD | 677 | 1 | 4% | 1% | -83% | -92% | -93% |
| SILVER | 661 | 2 | 3% | 1% | -65% | -94% | -93% |
| WTI | 634 | 3 | 3% | 1% | -46% | -94% | -96% |
| COPPER | 581 | 0 | 2% | 1% | -100% | -97% | -96% |
| PLATINUM | 553 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 513 | 1 | 1% | 0% | -82% | -98% | -98% |
| NATGAS | 510 | 3 | 3% | 2% | -45% | -96% | -94% |
| EURUSD | 494 | 3 | 3% | 2% | -43% | -77% | -76% |
| GBPUSD | 466 | 1 | 2% | 1% | -80% | -96% | -96% |
| USDJPY | 422 | 3 | 1% | 1% | -34% | -98% | -98% |
| AUDUSD | 67 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 58 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8603 | 35 | 3% | 2% | -53% | -90% | -89% |
| DOWN (bought NO) | 8493 | 30 | 3% | 2% | -59% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2000 | 10 | 2% | 1% | -17% | -77% | -77% |
| 0.05–0.1% | 2031 | 6 | 3% | 1% | -58% | -92% | -92% |
| 0.1–0.2% | 2932 | 9 | 4% | 2% | -62% | -91% | -91% |
| 0.2–0.5% | 3237 | 18 | 5% | 3% | -39% | -89% | -89% |
| Over 0.5% | 1257 | 5 | 6% | 2% | -59% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4344 | 20 | 4% | 2% | -47% | -87% | -87% |
| Morning (6am–12pm) | 3923 | 20 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 4113 | 10 | 3% | 1% | -71% | -91% | -91% |
| Evening (6pm–12am) | 4716 | 15 | 3% | 2% | -64% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,537 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 7:10:48 PM | ZEC | UP | 4.2 min | -0.691% | — | In play | — |
| 10/13 7:10:32 PM | XRP | UP | 4.5 min | -0.328% | — | In play | — |
| 10/13 7:10:32 PM | BNB | UP | 4.5 min | -0.184% | — | In play | — |
| 10/13 6:59:48 PM | GOLD | UP | 12 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/13 6:59:48 PM | AUDUSD | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:59:16 PM | USDJPY | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:59:01 PM | PLATINUM | DOWN | 58 sec | — | 10¢ | ❌ Lost | -$0.15 |
| 10/13 6:59:01 PM | SILVER | DOWN | 58 sec | — | 36¢ | ✅ Won | $14.00 |
| 10/13 6:58:43 PM | WTI | DOWN | 76 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:58:27 PM | ZEC | UP | 1.5 min | -0.347% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:57:41 PM | NEAR | UP | 2.3 min | -0.473% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:57:09 PM | XRP | UP | 2.8 min | -0.233% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:56:53 PM | SOL | UP | 3.1 min | -0.316% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:56:53 PM | BTC | UP | 3.1 min | -0.196% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:56:53 PM | HYPE | UP | 3.1 min | -0.303% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:56:35 PM | BNB | UP | 3.4 min | -0.150% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:54:44 PM | ETH | UP | 5.3 min | -0.363% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:54:44 PM | DOGE | UP | 5.3 min | -0.372% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:44:50 PM | NATGAS | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:44:50 PM | AUDUSD | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:44:34 PM | PLATINUM | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:44:18 PM | EURUSD | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:43:46 PM | GBPUSD | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:43:14 PM | SILVER | UP | 1.8 min | — | 1¢ | ❌ Lost | $0.00 |
| 10/13 6:43:14 PM | GOLD | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:42:09 PM | USDJPY | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:40:15 PM | BTC | DOWN | 4.7 min | +0.261% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:39:59 PM | NEAR | DOWN | 5.0 min | +0.730% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:39:44 PM | SOL | DOWN | 5.2 min | +0.414% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:39:44 PM | ZEC | DOWN | 5.2 min | +1.083% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
