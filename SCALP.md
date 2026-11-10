# Range-Scalp Bot

*Updated Tue Nov 10 15:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54653 | 47675 | 6978 (91) | 5 | $-14864.50 | -4.3% |
| **+10¢** | 40832 | 32688 | 8144 (121) | 6 | $-13801.76 | -5.4% |
| **+15¢** | 34230 | 25450 | 8780 (155) | 6 | $-12558.68 | -5.8% |
| **+20¢** | 30477 | 21265 | 9212 (204) | 6 | $-10982.07 | -5.7% |
| **+10¢ (15¢ stop)** | 66583 | 66469 | 114 (70) | 0 | $-24598.72 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 15:12 | +10 stop | BNB | DOWN | 0.67 | 0.79 | 0.92 |
| 11-10 15:12 | +10 stop | DOGE | DOWN | 0.71 | 0.84 | 1.05 |
| 11-10 15:11 | +5 | BNB | UP | 0.67 | open |  |
| 11-10 15:11 | +10 stop | DOGE | UP | 0.58 | 0.38 | -2.35 |
| 11-10 15:11 | +20 | DOGE | UP | 0.59 | open |  |
| 11-10 15:11 | +15 | DOGE | UP | 0.59 | open |  |
| 11-10 15:11 | +10 | DOGE | UP | 0.58 | open |  |
| 11-10 15:11 | +5 | DOGE | UP | 0.58 | open |  |
| 11-10 15:10 | +5 | ETH | UP | 0.67 | open |  |
| 11-10 15:10 | +5 | XRP | UP | 0.61 | open |  |
| 11-10 15:09 | +10 stop | ZEC | DOWN | 0.46 | 0.27 | -2.22 |
| 11-10 15:09 | +10 stop | BNB | UP | 0.71 | 0.43 | -3.13 |
| 11-10 15:09 | +15 | BNB | UP | 0.71 | open |  |
| 11-10 15:09 | +10 | BNB | UP | 0.71 | open |  |
| 11-10 15:09 | +5 | BNB | UP | 0.70 | 0.80 | 0.73 |
| 11-10 15:09 | +5 | XRP | UP | 0.61 | 0.71 | 0.68 |
| 11-10 15:09 | +5 | ZEC | UP | 0.62 | 0.70 | 0.48 |
| 11-10 15:08 | +5 | ETH | UP | 0.70 | 0.75 | 0.21 |
| 11-10 15:08 | +10 stop | XRP | UP | 0.63 | 0.31 | -3.52 |
| 11-10 15:08 | +5 | XRP | UP | 0.61 | 0.68 | 0.37 |
| 11-10 15:08 | +10 stop | NEAR | UP | 0.47 | 0.26 | -2.42 |
| 11-10 15:07 | +10 stop | NEAR | DOWN | 0.47 | 0.57 | 0.64 |
| 11-10 15:07 | +10 stop | ZEC | UP | 0.67 | 0.44 | -2.64 |
| 11-10 15:07 | +20 | ZEC | UP | 0.67 | open |  |
| 11-10 15:07 | +15 | ZEC | UP | 0.67 | open |  |
| 11-10 15:07 | +10 | ZEC | UP | 0.67 | open |  |
| 11-10 15:07 | +5 | ZEC | UP | 0.67 | 0.72 | 0.19 |
| 11-10 15:06 | +10 stop | BNB | UP | 0.62 | 0.77 | 1.20 |
| 11-10 15:06 | +20 | BNB | UP | 0.62 | open |  |
| 11-10 15:06 | +15 | BNB | UP | 0.62 | 0.77 | 1.20 |
| 11-10 15:06 | +10 | BNB | UP | 0.62 | 0.77 | 1.20 |
| 11-10 15:06 | +5 | BNB | UP | 0.62 | 0.71 | 0.58 |
| 11-10 15:06 | +10 stop | NEAR | UP | 0.59 | 0.43 | -1.95 |
| 11-10 15:06 | +20 | NEAR | UP | 0.60 | open |  |
| 11-10 15:06 | +15 | NEAR | UP | 0.60 | open |  |
| 11-10 15:06 | +10 | NEAR | UP | 0.60 | open |  |
| 11-10 15:06 | +5 | NEAR | UP | 0.60 | open |  |
| 11-10 15:05 | +5 | BNB | UP | 0.70 | 0.75 | 0.21 |
| 11-10 15:05 | +10 stop | XRP | UP | 0.71 | 0.56 | -1.83 |
| 11-10 15:05 | +20 | XRP | UP | 0.71 | open |  |
