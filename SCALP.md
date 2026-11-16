# Range-Scalp Bot

*Updated Mon Nov 16 07:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61714 | 53854 | 7860 (115) | 4 | $-16595.40 | -4.3% |
| **+10¢** | 46100 | 36891 | 9209 (157) | 4 | $-15527.40 | -5.4% |
| **+15¢** | 38628 | 28694 | 9934 (196) | 5 | $-14155.56 | -5.8% |
| **+20¢** | 34436 | 24017 | 10419 (249) | 5 | $-12368.65 | -5.7% |
| **+10¢ (15¢ stop)** | 75106 | 74952 | 154 (90) | 0 | $-27642.73 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 07:22 | +10 stop | BTC | UP | 0.69 | 0.86 | 1.46 |
| 11-16 07:22 | +10 | BTC | UP | 0.71 | 0.86 | 1.26 |
| 11-16 07:22 | +5 | BTC | UP | 0.71 | 0.77 | 0.32 |
| 11-16 07:22 | +10 stop | XRP | UP | 0.65 | 0.76 | 0.81 |
| 11-16 07:22 | +20 | XRP | UP | 0.65 | 0.86 | 1.85 |
| 11-16 07:22 | +15 | XRP | UP | 0.65 | 0.86 | 1.85 |
| 11-16 07:22 | +10 | XRP | UP | 0.65 | 0.76 | 0.81 |
| 11-16 07:22 | +5 | XRP | UP | 0.65 | 0.76 | 0.81 |
| 11-16 07:22 | +10 stop | NEAR | UP | 0.70 | 0.87 | 1.47 |
| 11-16 07:22 | +10 stop | HYPE | UP | 0.71 | 0.55 | -1.93 |
| 11-16 07:22 | +10 stop | DOGE | DOWN | 0.64 | 0.45 | -2.25 |
| 11-16 07:22 | +20 | DOGE | DOWN | 0.64 | open |  |
| 11-16 07:22 | +15 | DOGE | DOWN | 0.66 | open |  |
| 11-16 07:22 | +10 | DOGE | DOWN | 0.67 | open |  |
| 11-16 07:22 | +5 | DOGE | DOWN | 0.68 | open |  |
| 11-16 07:21 | +10 stop | ETH | DOWN | 0.54 | 0.31 | -2.63 |
| 11-16 07:21 | +20 | ETH | DOWN | 0.54 | open |  |
| 11-16 07:21 | +15 | ETH | DOWN | 0.54 | open |  |
| 11-16 07:21 | +10 | ETH | DOWN | 0.54 | open |  |
| 11-16 07:21 | +5 | ETH | DOWN | 0.54 | open |  |
| 11-16 07:21 | +10 stop | BNB | UP | 0.68 | 0.78 | 0.71 |
| 11-16 07:21 | +20 | BNB | UP | 0.68 | 0.90 | 1.98 |
| 11-16 07:21 | +15 | BNB | UP | 0.68 | 0.84 | 1.34 |
| 11-16 07:21 | +10 | BNB | UP | 0.68 | 0.78 | 0.71 |
| 11-16 07:21 | +5 | BNB | UP | 0.68 | 0.77 | 0.61 |
| 11-16 07:21 | +10 stop | ZEC | UP | 0.69 | 0.79 | 0.73 |
| 11-16 07:21 | +20 | ZEC | UP | 0.69 | 0.89 | 1.78 |
| 11-16 07:21 | +15 | ZEC | UP | 0.69 | 0.84 | 1.25 |
| 11-16 07:21 | +10 | ZEC | UP | 0.69 | 0.79 | 0.73 |
| 11-16 07:21 | +5 | ZEC | UP | 0.69 | 0.74 | 0.21 |
| 11-16 07:21 | +10 stop | BTC | DOWN | 0.51 | 0.61 | 0.65 |
| 11-16 07:21 | +20 | BTC | DOWN | 0.51 | open |  |
| 11-16 07:21 | +15 | BTC | DOWN | 0.51 | open |  |
| 11-16 07:21 | +10 | BTC | DOWN | 0.51 | 0.61 | 0.65 |
| 11-16 07:21 | +5 | BTC | DOWN | 0.51 | 0.61 | 0.65 |
| 11-16 07:21 | +10 stop | HYPE | DOWN | 0.59 | 0.40 | -2.24 |
| 11-16 07:21 | +20 | HYPE | DOWN | 0.59 | open |  |
| 11-16 07:21 | +15 | HYPE | DOWN | 0.59 | open |  |
| 11-16 07:21 | +10 | HYPE | DOWN | 0.60 | open |  |
| 11-16 07:21 | +5 | HYPE | DOWN | 0.60 | open |  |
