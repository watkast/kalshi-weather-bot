# Range-Scalp Bot

*Updated Mon Nov 23 22:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70180 | 61245 | 8935 (147) | 1 | $-18858.63 | -4.3% |
| **+10¢** | 52364 | 41928 | 10436 (190) | 1 | $-17503.51 | -5.3% |
| **+15¢** | 43876 | 32637 | 11239 (246) | 1 | $-15590.06 | -5.7% |
| **+20¢** | 39063 | 27234 | 11829 (311) | 1 | $-13964.18 | -5.7% |
| **+10¢ (15¢ stop)** | 85477 | 85281 | 196 (118) | 0 | $-31445.13 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 22:06 | +10 | BNB | DOWN | 0.62 | 0.73 | 0.79 |
| 11-23 22:06 | +10 stop | XRP | DOWN | 0.55 | 0.72 | 1.37 |
| 11-23 22:06 | +5 | BTC | DOWN | 0.66 | 0.73 | 0.40 |
| 11-23 22:06 | +5 | BNB | DOWN | 0.60 | 0.73 | 0.99 |
| 11-23 22:05 | +10 stop | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 11-23 22:05 | +10 | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 11-23 22:05 | +5 | SOL | DOWN | 0.64 | 0.70 | 0.28 |
| 11-23 22:05 | +10 | BNB | DOWN | 0.53 | 0.63 | 0.68 |
| 11-23 22:05 | +5 | BNB | DOWN | 0.53 | 0.59 | 0.28 |
| 11-23 22:05 | +5 | BTC | DOWN | 0.54 | 0.60 | 0.25 |
| 11-23 22:05 | +10 | DOGE | DOWN | 0.71 | 0.88 | 1.47 |
| 11-23 22:04 | +5 | DOGE | DOWN | 0.65 | 0.77 | 0.91 |
| 11-23 22:04 | +10 stop | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 11-23 22:04 | +10 stop | BTC | DOWN | 0.66 | 0.82 | 1.33 |
| 11-23 22:04 | +10 stop | ZEC | DOWN | 0.55 | 0.76 | 1.79 |
| 11-23 22:04 | +10 stop | BNB | UP | 0.45 | 0.25 | -2.32 |
| 11-23 22:04 | +10 stop | XRP | UP | 0.56 | 0.39 | -2.05 |
| 11-23 22:04 | +10 | XRP | UP | 0.56 | open |  |
| 11-23 22:03 | +10 stop | NEAR | DOWN | 0.61 | 0.72 | 0.78 |
| 11-23 22:03 | +5 | NEAR | DOWN | 0.61 | 0.72 | 0.78 |
| 11-23 22:03 | +10 stop | DOGE | DOWN | 0.43 | 0.55 | 0.84 |
| 11-23 22:03 | +10 stop | HYPE | DOWN | 0.59 | 0.71 | 0.88 |
| 11-23 22:02 | +10 stop | DOGE | UP | 0.65 | 0.45 | -2.34 |
| 11-23 22:02 | +5 | XRP | UP | 0.70 | open |  |
| 11-23 22:01 | +10 stop | DOGE | DOWN | 0.56 | 0.41 | -1.85 |
| 11-23 22:01 | +20 | DOGE | DOWN | 0.56 | 0.77 | 1.79 |
| 11-23 22:01 | +15 | DOGE | DOWN | 0.56 | 0.77 | 1.79 |
| 11-23 22:01 | +10 | DOGE | DOWN | 0.56 | 0.68 | 0.86 |
| 11-23 22:01 | +5 | DOGE | DOWN | 0.56 | 0.62 | 0.25 |
| 11-23 22:01 | +10 stop | BNB | DOWN | 0.55 | 0.38 | -2.05 |
| 11-23 22:01 | +20 | BNB | DOWN | 0.55 | 0.84 | 2.62 |
| 11-23 22:01 | +15 | BNB | DOWN | 0.55 | 0.73 | 1.48 |
| 11-23 22:01 | +10 | BNB | DOWN | 0.55 | 0.67 | 0.86 |
| 11-23 22:01 | +5 | BNB | DOWN | 0.55 | 0.67 | 0.86 |
| 11-23 22:01 | +10 stop | NEAR | DOWN | 0.65 | 0.46 | -2.24 |
| 11-23 22:01 | +20 | NEAR | DOWN | 0.65 | 0.87 | 1.96 |
| 11-23 22:01 | +15 | NEAR | DOWN | 0.65 | 0.83 | 1.54 |
| 11-23 22:01 | +10 | NEAR | DOWN | 0.65 | 0.77 | 0.91 |
| 11-23 22:01 | +5 | NEAR | DOWN | 0.65 | 0.71 | 0.29 |
| 11-23 22:01 | +10 stop | SOL | DOWN | 0.59 | 0.73 | 1.09 |
