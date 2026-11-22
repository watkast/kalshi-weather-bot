# Range-Scalp Bot

*Updated Sun Nov 22 00:48 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68035 | 59381 | 8654 (138) | 2 | $-18211.66 | -4.3% |
| **+10¢** | 50793 | 40684 | 10109 (181) | 4 | $-16878.92 | -5.3% |
| **+15¢** | 42575 | 31676 | 10899 (230) | 7 | $-15150.16 | -5.7% |
| **+20¢** | 37900 | 26445 | 11455 (288) | 8 | $-13475.93 | -5.7% |
| **+10¢ (15¢ stop)** | 82811 | 82633 | 178 (110) | 4 | $-30395.86 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 00:48 | +10 stop | ZEC | UP | 0.59 | open |  |
| 11-22 00:48 | +10 | ZEC | UP | 0.59 | open |  |
| 11-22 00:47 | +10 stop | BNB | UP | 0.51 | open |  |
| 11-22 00:47 | +20 | BNB | UP | 0.51 | open |  |
| 11-22 00:47 | +15 | BNB | UP | 0.51 | open |  |
| 11-22 00:47 | +10 | BNB | UP | 0.51 | open |  |
| 11-22 00:47 | +5 | BNB | UP | 0.51 | 0.56 | 0.14 |
| 11-22 00:47 | +5 | ZEC | UP | 0.58 | open |  |
| 11-22 00:47 | +10 stop | DOGE | UP | 0.52 | 0.62 | 0.65 |
| 11-22 00:47 | +20 | DOGE | UP | 0.52 | open |  |
| 11-22 00:47 | +15 | DOGE | UP | 0.52 | open |  |
| 11-22 00:47 | +10 | DOGE | UP | 0.52 | 0.62 | 0.65 |
| 11-22 00:47 | +5 | DOGE | UP | 0.52 | 0.62 | 0.65 |
| 11-22 00:47 | +5 | XRP | DOWN | 0.50 | 0.56 | 0.24 |
| 11-22 00:47 | +5 | SOL | DOWN | 0.54 | 0.63 | 0.55 |
| 11-22 00:47 | +5 | HYPE | DOWN | 0.66 | 0.71 | 0.19 |
| 11-22 00:47 | +5 | XRP | DOWN | 0.58 | 0.63 | 0.15 |
| 11-22 00:47 | +5 | BTC | DOWN | 0.64 | open |  |
| 11-22 00:47 | +10 stop | ZEC | UP | 0.50 | 0.61 | 0.75 |
| 11-22 00:47 | +20 | ZEC | UP | 0.50 | open |  |
| 11-22 00:47 | +15 | ZEC | UP | 0.49 | open |  |
| 11-22 00:47 | +10 | ZEC | UP | 0.49 | 0.61 | 0.85 |
| 11-22 00:47 | +5 | ZEC | UP | 0.49 | 0.55 | 0.24 |
| 11-22 00:46 | +10 stop | ETH | DOWN | 0.59 | open |  |
| 11-22 00:46 | +20 | ETH | DOWN | 0.60 | open |  |
| 11-22 00:46 | +15 | ETH | DOWN | 0.60 | open |  |
| 11-22 00:46 | +10 | ETH | DOWN | 0.60 | open |  |
| 11-22 00:46 | +5 | ETH | DOWN | 0.60 | 0.68 | 0.47 |
| 11-22 00:46 | +10 stop | NEAR | UP | 0.70 | 0.86 | 1.40 |
| 11-22 00:46 | +20 | NEAR | UP | 0.70 | open |  |
| 11-22 00:46 | +15 | NEAR | UP | 0.70 | 0.86 | 1.40 |
| 11-22 00:46 | +10 | NEAR | UP | 0.69 | 0.86 | 1.46 |
| 11-22 00:46 | +5 | NEAR | UP | 0.69 | 0.86 | 1.46 |
| 11-22 00:46 | +10 stop | HYPE | DOWN | 0.50 | 0.68 | 1.46 |
| 11-22 00:46 | +20 | HYPE | DOWN | 0.50 | 0.71 | 1.77 |
| 11-22 00:46 | +15 | HYPE | DOWN | 0.50 | 0.68 | 1.46 |
| 11-22 00:46 | +10 | HYPE | DOWN | 0.50 | 0.68 | 1.46 |
| 11-22 00:46 | +5 | HYPE | DOWN | 0.50 | 0.55 | 0.14 |
| 11-22 00:46 | +10 stop | BTC | DOWN | 0.56 | 0.66 | 0.66 |
| 11-22 00:46 | +20 | BTC | DOWN | 0.56 | open |  |
