# Range-Scalp Bot

*Updated Mon Oct 26 16:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35088 | 30631 | 4457 (43) | 1 | $-9758.44 | -4.4% |
| **+10¢** | 26259 | 21106 | 5153 (65) | 3 | $-8555.62 | -5.2% |
| **+15¢** | 21968 | 16420 | 5548 (89) | 5 | $-7669.51 | -5.6% |
| **+20¢** | 19474 | 13659 | 5815 (112) | 5 | $-6742.65 | -5.5% |
| **+10¢ (15¢ stop)** | 42955 | 42893 | 62 (33) | 4 | $-16262.69 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 16:19 | +5 | BTC | DOWN | 0.60 | 0.69 | 0.58 |
| 10-26 16:19 | +5 | SOL | DOWN | 0.63 | 0.69 | 0.27 |
| 10-26 16:18 | +10 stop | ZEC | DOWN | 0.71 | open |  |
| 10-26 16:18 | +10 stop | BNB | DOWN | 0.69 | open |  |
| 10-26 16:17 | +10 stop | SOL | DOWN | 0.69 | open |  |
| 10-26 16:17 | +20 | SOL | DOWN | 0.68 | open |  |
| 10-26 16:17 | +15 | SOL | DOWN | 0.69 | open |  |
| 10-26 16:17 | +10 | SOL | DOWN | 0.69 | open |  |
| 10-26 16:17 | +5 | SOL | DOWN | 0.69 | 0.75 | 0.31 |
| 10-26 16:17 | +10 | ZEC | DOWN | 0.61 | 0.73 | 0.89 |
| 10-26 16:17 | +5 | ZEC | DOWN | 0.61 | 0.68 | 0.37 |
| 10-26 16:16 | +10 stop | BTC | DOWN | 0.68 | open |  |
| 10-26 16:16 | +20 | BTC | DOWN | 0.68 | open |  |
| 10-26 16:16 | +15 | BTC | DOWN | 0.68 | open |  |
| 10-26 16:16 | +10 | BTC | DOWN | 0.68 | open |  |
| 10-26 16:16 | +5 | BTC | DOWN | 0.68 | 0.73 | 0.20 |
| 10-26 16:16 | +10 stop | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 10-26 16:16 | +20 | NEAR | DOWN | 0.70 | open |  |
| 10-26 16:16 | +15 | NEAR | DOWN | 0.70 | open |  |
| 10-26 16:16 | +10 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 10-26 16:16 | +5 | NEAR | DOWN | 0.70 | 0.76 | 0.32 |
| 10-26 16:16 | +10 stop | BNB | DOWN | 0.69 | 0.48 | -2.43 |
| 10-26 16:16 | +20 | BNB | DOWN | 0.69 | open |  |
| 10-26 16:16 | +15 | BNB | DOWN | 0.69 | open |  |
| 10-26 16:16 | +10 | BNB | DOWN | 0.69 | open |  |
| 10-26 16:16 | +5 | BNB | DOWN | 0.69 | open |  |
| 10-26 16:15 | +10 stop | DOGE | DOWN | 0.58 | 0.75 | 1.38 |
| 10-26 16:15 | +20 | DOGE | DOWN | 0.58 | 0.79 | 1.80 |
| 10-26 16:15 | +15 | DOGE | DOWN | 0.58 | 0.75 | 1.38 |
| 10-26 16:15 | +10 | DOGE | DOWN | 0.58 | 0.75 | 1.38 |
| 10-26 16:15 | +5 | DOGE | DOWN | 0.58 | 0.75 | 1.38 |
| 10-26 16:15 | +10 stop | ZEC | DOWN | 0.68 | 0.52 | -1.94 |
| 10-26 16:15 | +20 | ZEC | DOWN | 0.68 | open |  |
| 10-26 16:15 | +15 | ZEC | DOWN | 0.67 | open |  |
| 10-26 16:15 | +10 | ZEC | DOWN | 0.66 | 0.77 | 0.82 |
| 10-26 16:15 | +5 | ZEC | DOWN | 0.64 | 0.75 | 0.76 |
| 10-26 16:12 | +10 stop | HYPE | UP | 0.38 | 0.62 | 2.06 |
| 10-26 16:12 | +5 | HYPE | UP | 0.38 | 0.62 | 2.06 |
| 10-26 16:12 | +10 stop | NEAR | DOWN | 0.61 | 0.91 | 2.81 |
| 10-26 16:12 | +5 | NEAR | DOWN | 0.61 | 0.67 | 0.27 |
