# 15-Minute 1¢ Study

*Updated Wed Oct 21, 5:50 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2235 finished bets | 1% | $83.55 | +33% | +3.74¢ | $46.50 / $37.05 |

*Expect about **96 buys a day** (~$14.44/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2068 | $64.50 | +28% |
| Volatility model ≥ 2%, hold to the close | 4096 | -$25.90 | -5% |
| Momentum model ≥ 2%, hold to the close | 3456 | -$29.40 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 26536 | 26529 | 97 (0%) | 1.07% | -$1,874.50 (-58%) | Hold to the close: -$1,874.50 (-58%) |

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
| Volatility model | 17202 | 4.6% | 0.4% (69) | -667% | ❌ Worse |
| Momentum model | 17202 | 4.6% | 0.4% (69) | -690% | ❌ Worse |
| Mean-reversion model | 17202 | 7.8% | 0.4% (69) | -806% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17202 | 69 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4096 | 34 | -5% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2235 | 24 | +33% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1284 | 16 | +74% | -61% | -59% | -56% |
| Momentum model ≥ 2% | 3456 | 27 | -7% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2068 | 21 | +28% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1360 | 14 | +40% | -68% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6792 | 45 | -28% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4739 | 37 | -14% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3148 | 25 | -10% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17400 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6321 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2808 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 26529 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 97 | 0% | -$1,874.50 | -58% | — |
| Sell at 2¢ | 963 | 4% | -$2,842.12 | -88% | 46 sec |
| Sell at 3¢ | 654 | 2% | -$2,837.44 | -88% | 48 sec |
| Sell at 5¢ | 463 | 2% | -$2,791.55 | -86% | 56 sec |
| Sell at 10¢ | 282 | 1% | -$2,695.08 | -83% | 64 sec |
| Sell at 25¢ | 154 | 1% | -$2,498.76 | -77% | 80 sec |
| Sell at 50¢ | 99 | 0% | -$2,270.25 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1071 | 6 | 10% | 4% | -46% | -81% | -84% |
| 2–5 min | 8548 | 43 | 7% | 3% | -50% | -87% | -87% |
| 1–2 min | 6774 | 25 | 3% | 1% | -60% | -93% | -92% |
| Under 1 min | 10132 | 23 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1952 | 11 | 5% | 2% | -30% | -90% | -90% |
| BNB | 1945 | 10 | 5% | 2% | -37% | -83% | -82% |
| HYPE | 1943 | 6 | 5% | 3% | -62% | -89% | -87% |
| ETH | 1934 | 10 | 6% | 3% | -38% | -87% | -86% |
| DOGE | 1932 | 3 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1931 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1925 | 7 | 3% | 1% | -55% | -88% | -88% |
| NEAR | 1919 | 11 | 6% | 3% | -26% | -79% | -79% |
| BTC | 1919 | 11 | 5% | 2% | -23% | -88% | -90% |
| GOLD | 1035 | 2 | 3% | 1% | -77% | -81% | -83% |
| SILVER | 997 | 4 | 3% | 1% | -54% | -82% | -82% |
| WTI | 975 | 3 | 3% | 1% | -64% | -94% | -95% |
| PLATINUM | 868 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 864 | 3 | 2% | 1% | -68% | -76% | -75% |
| NATGAS | 798 | 5 | 2% | 1% | -42% | -85% | -84% |
| EURUSD | 794 | 3 | 2% | 1% | -65% | -84% | -84% |
| PALLADIUM | 784 | 2 | 1% | 0% | -76% | -86% | -86% |
| GBPUSD | 744 | 1 | 2% | 1% | -87% | -97% | -97% |
| USDJPY | 704 | 3 | 1% | 1% | -60% | -99% | -98% |
| AUDUSD | 307 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 259 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13339 | 49 | 4% | 2% | -58% | -88% | -87% |
| DOWN (bought NO) | 13190 | 48 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2922 | 15 | 2% | 1% | -14% | -78% | -77% |
| 0.05–0.1% | 3021 | 11 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 4432 | 14 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 5066 | 25 | 6% | 3% | -46% | -88% | -87% |
| Over 0.5% | 1956 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6827 | 28 | 4% | 2% | -53% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6157 | 19 | 3% | 1% | -64% | -88% | -89% |
| Evening (6pm–12am) | 7332 | 21 | 3% | 2% | -67% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,740 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/21 5:44:53 AM | USDCAD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:44:53 AM | USDJPY | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:44:37 AM | EURUSD | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:44:37 AM | NEAR | UP | 22 sec | -0.127% | 0¢ | ❌ Lost | $0.00 |
| 10/21 5:44:37 AM | PLATINUM | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:44:37 AM | SOL | UP | 22 sec | -0.039% | 0¢ | ❌ Lost | $0.00 |
| 10/21 5:44:37 AM | AUDUSD | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:44:21 AM | BTC | UP | 38 sec | -0.010% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:44:21 AM | XRP | UP | 38 sec | -0.125% | 0¢ | ❌ Lost | $0.00 |
| 10/21 5:44:05 AM | DOGE | UP | 55 sec | -0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 5:43:17 AM | GBPUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:43:17 AM | SILVER | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 5:43:17 AM | NATGAS | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:43:01 AM | COPPER | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:41:23 AM | GOLD | DOWN | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 5:40:52 AM | ETH | UP | 4.1 min | -0.196% | 39¢ | ❌ Lost | -$0.15 |
| 10/21 5:39:43 AM | BNB | UP | 5.3 min | -0.205% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 5:39:43 AM | HYPE | UP | 5.3 min | -0.400% | 0¢ | ❌ Lost | $0.00 |
| 10/21 5:29:33 AM | XRP | UP | 27 sec | -0.140% | 0¢ | ❌ Lost | $0.00 |
| 10/21 5:29:33 AM | NEAR | UP | 27 sec | -0.216% | 0¢ | ❌ Lost | $0.00 |
| 10/21 5:29:33 AM | SOL | UP | 27 sec | -0.046% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:29:17 AM | EURUSD | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:29:02 AM | DOGE | DOWN | 57 sec | +0.046% | 26¢ | ❌ Lost | -$0.15 |
| 10/21 5:29:02 AM | ZEC | DOWN | 57 sec | +0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 5:28:46 AM | USDCAD | DOWN | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:28:46 AM | USDJPY | UP | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:28:30 AM | HYPE | DOWN | 89 sec | +0.108% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 5:27:58 AM | BTC | DOWN | 2.0 min | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 5:27:58 AM | GBPUSD | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:26:54 AM | ETH | DOWN | 3.1 min | +0.153% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
