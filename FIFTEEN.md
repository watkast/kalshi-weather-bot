# 15-Minute 1¢ Study

*Updated Fri Oct 2, 7:06 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 171 finished bets | 1% | $2.80 | +11% | +1.64¢ | $15.40 / -$12.60 |

*Expect about **35 buys a day** (~$5.20/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 389 | $0.90 | +2% |
| Momentum model ≥ 5%, sell at 50¢ | 389 | -$6.35 | -15% |
| Volatility model ≥ 5%, sell at 25¢ | 385 | -$10.55 | -26% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6108 | 6102 | 23 (0%) | 1.07% | -$416.90 (-56%) | Hold to the close: -$416.90 (-56%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 3571 | 3.9% | 0.3% (11) | -677% | ❌ Worse |
| Momentum model | 3571 | 4.0% | 0.3% (11) | -720% | ❌ Worse |
| Mean-reversion model | 3571 | 6.9% | 0.3% (11) | -828% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3571 | 11 | -60% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 761 | 5 | -24% | -65% | -65% | -60% |
| Volatility model ≥ 5% | 385 | 2 | -32% | -44% | -44% | -39% |
| Volatility model ≥ 10% | 224 | 2 | +36% | -9% | -11% | -3% |
| Momentum model ≥ 2% | 670 | 4 | -28% | -64% | -67% | -63% |
| Momentum model ≥ 5% | 389 | 3 | +2% | -49% | -53% | -47% |
| Momentum model ≥ 10% | 262 | 2 | +12% | -31% | -32% | -26% |
| Mean-reversion model ≥ 2% | 1360 | 7 | -44% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 907 | 6 | -27% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 585 | 4 | -22% | -77% | -80% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3768 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1779 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6102 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 23 | 0% | -$416.90 | -56% | — |
| Sell at 2¢ | 242 | 4% | -$661.98 | -90% | 43 sec |
| Sell at 3¢ | 152 | 2% | -$665.62 | -90% | 48 sec |
| Sell at 5¢ | 113 | 2% | -$651.45 | -88% | 64 sec |
| Sell at 10¢ | 74 | 1% | -$613.96 | -83% | 81 sec |
| Sell at 25¢ | 39 | 1% | -$567.81 | -77% | 1.6 min |
| Sell at 50¢ | 21 | 0% | -$513.15 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 168 | 2 | 12% | 3% | +13% | -79% | -89% |
| 2–5 min | 1992 | 12 | 8% | 4% | -41% | -86% | -87% |
| 1–2 min | 1591 | 6 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 2348 | 3 | 1% | 0% | -81% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 426 | 2 | 4% | 1% | -37% | -89% | -90% |
| ZEC | 422 | 2 | 5% | 3% | -43% | -88% | -90% |
| ETH | 420 | 2 | 6% | 3% | -41% | -86% | -85% |
| HYPE | 420 | 2 | 5% | 4% | -41% | -87% | -84% |
| BNB | 419 | 0 | 4% | 1% | -100% | -91% | -93% |
| BTC | 418 | 1 | 7% | 3% | -69% | -84% | -88% |
| XRP | 416 | 3 | 1% | 1% | -5% | -65% | -65% |
| SOL | 415 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 412 | 1 | 6% | 2% | -67% | -85% | -88% |
| GOLD | 304 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 285 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 271 | 2 | 3% | 1% | -23% | -94% | -96% |
| COPPER | 254 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 226 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 223 | 2 | 4% | 2% | -16% | -94% | -92% |
| PALLADIUM | 216 | 1 | 2% | 1% | -57% | -96% | -98% |
| GBPUSD | 195 | 1 | 4% | 2% | -52% | -93% | -93% |
| EURUSD | 195 | 1 | 5% | 3% | -52% | -91% | -89% |
| USDJPY | 165 | 3 | 2% | 2% | +70% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3105 | 14 | 4% | 2% | -47% | -91% | -91% |
| DOWN (bought NO) | 2997 | 9 | 4% | 2% | -66% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 464 | 2 | 1% | 1% | -19% | -56% | -55% |
| 0.05–0.1% | 532 | 0 | 3% | 1% | -100% | -90% | -93% |
| 0.1–0.2% | 920 | 2 | 4% | 2% | -71% | -91% | -91% |
| 0.2–0.5% | 1264 | 5 | 6% | 3% | -56% | -87% | -87% |
| Over 0.5% | 586 | 4 | 7% | 3% | -29% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1474 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1640 | 9 | 5% | 3% | -38% | -90% | -88% |
| Afternoon (12–6pm) | 1305 | 3 | 4% | 1% | -73% | -83% | -85% |
| Evening (6pm–12am) | 1683 | 6 | 3% | 2% | -59% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,135 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 6:59:58 PM | HYPE | UP | 1 sec | -0.002% | 0¢ | ❌ Lost | $0.00 |
| 10/2 6:59:41 PM | WTI | DOWN | 19 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 6:59:09 PM | DOGE | UP | 51 sec | -0.074% | 0¢ | ❌ Lost | $0.00 |
| 10/2 6:58:54 PM | BTC | DOWN | 66 sec | +0.032% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 6:58:54 PM | ETH | DOWN | 66 sec | +0.035% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:58:54 PM | NEAR | UP | 66 sec | -0.313% | 0¢ | ❌ Lost | $0.00 |
| 10/2 6:58:54 PM | XRP | UP | 66 sec | -0.107% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:58:20 PM | ZEC | DOWN | 1.7 min | +0.245% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:58:20 PM | SOL | UP | 1.7 min | -0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 6:44:45 PM | XRP | DOWN | 14 sec | +0.081% | 0¢ | ❌ Lost | $0.00 |
| 10/2 6:44:39 PM | SOL | DOWN | 20 sec | +0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/2 6:44:15 PM | DOGE | UP | 44 sec | -0.149% | 0¢ | ❌ Lost | $0.00 |
| 10/2 6:43:31 PM | ETH | DOWN | 89 sec | +0.064% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:43:25 PM | BTC | DOWN | 1.6 min | +0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 6:43:15 PM | BNB | DOWN | 1.8 min | +0.039% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:42:56 PM | ZEC | UP | 2.1 min | -0.591% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:41:49 PM | HYPE | UP | 3.2 min | -0.647% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 6:29:35 PM | BNB | UP | 24 sec | -0.053% | 0¢ | ❌ Lost | $0.00 |
| 10/2 6:29:09 PM | BTC | DOWN | 50 sec | +0.064% | 0¢ | ❌ Lost | $0.00 |
| 10/2 6:28:41 PM | NEAR | DOWN | 79 sec | +0.284% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:27:30 PM | HYPE | DOWN | 2.5 min | +0.562% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:27:28 PM | ETH | DOWN | 2.5 min | +0.100% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 6:27:18 PM | DOGE | DOWN | 2.7 min | +0.214% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 6:27:16 PM | XRP | DOWN | 2.7 min | +0.222% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 6:27:16 PM | SOL | DOWN | 2.7 min | +0.189% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:25:19 PM | ZEC | DOWN | 4.7 min | +1.235% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:14:54 PM | BTC | UP | 6 sec | -0.001% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:14:52 PM | DOGE | DOWN | 8 sec | +0.090% | 0¢ | ❌ Lost | $0.00 |
| 10/2 6:14:12 PM | BNB | DOWN | 48 sec | +0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/2 6:13:57 PM | SOL | DOWN | 63 sec | +0.081% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
