# Range-Scalp Bot

*Updated Tue Nov 10 16:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54713 | 47727 | 6986 (91) | 0 | $-14882.12 | -4.3% |
| **+10¢** | 40879 | 32727 | 8152 (121) | 0 | $-13811.52 | -5.4% |
| **+15¢** | 34269 | 25483 | 8786 (155) | 0 | $-12549.91 | -5.8% |
| **+20¢** | 30512 | 21293 | 9219 (204) | 0 | $-10968.70 | -5.7% |
| **+10¢ (15¢ stop)** | 66651 | 66537 | 114 (70) | 0 | $-24649.03 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 16:12 | +10 stop | NEAR | DOWN | 0.47 | 0.61 | 1.05 |
| 11-10 16:11 | +5 | XRP | UP | 0.70 | 0.92 | 1.94 |
| 11-10 16:11 | +10 stop | BNB | UP | 0.70 | 0.80 | 0.73 |
| 11-10 16:11 | +5 | BNB | UP | 0.71 | 0.80 | 0.63 |
| 11-10 16:11 | +5 | NEAR | DOWN | 0.61 | yes | -6.27 |
| 11-10 16:11 | +10 stop | BTC | UP | 0.50 | 0.76 | 2.29 |
| 11-10 16:11 | +15 | BTC | UP | 0.50 | 0.76 | 2.29 |
| 11-10 16:11 | +10 | BTC | UP | 0.50 | 0.76 | 2.29 |
| 11-10 16:11 | +5 | BTC | UP | 0.52 | 0.57 | 0.14 |
| 11-10 16:11 | +5 | NEAR | UP | 0.39 | 0.53 | 1.05 |
| 11-10 16:10 | +10 stop | NEAR | UP | 0.55 | 0.37 | -2.15 |
| 11-10 16:10 | +10 | NEAR | UP | 0.55 | 0.77 | 1.89 |
| 11-10 16:10 | +5 | NEAR | UP | 0.54 | 0.60 | 0.25 |
| 11-10 16:10 | +5 | SOL | DOWN | 0.52 | 0.63 | 0.75 |
| 11-10 16:09 | +10 stop | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 11-10 16:09 | +10 | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 11-10 16:09 | +10 stop | ZEC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-10 16:09 | +5 | ZEC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-10 16:09 | +10 stop | DOGE | UP | 0.63 | 0.74 | 0.79 |
| 11-10 16:09 | +20 | DOGE | UP | 0.63 | 0.84 | 1.83 |
| 11-10 16:09 | +15 | DOGE | UP | 0.63 | 0.84 | 1.83 |
| 11-10 16:09 | +10 | DOGE | UP | 0.63 | 0.74 | 0.79 |
| 11-10 16:09 | +5 | DOGE | UP | 0.63 | 0.74 | 0.79 |
| 11-10 16:09 | +10 stop | BTC | UP | 0.52 | 0.70 | 1.47 |
| 11-10 16:09 | +15 | BTC | UP | 0.54 | 0.70 | 1.27 |
| 11-10 16:09 | +10 | BTC | UP | 0.55 | 0.70 | 1.17 |
| 11-10 16:09 | +5 | BTC | UP | 0.55 | 0.70 | 1.17 |
| 11-10 16:09 | +10 | ZEC | DOWN | 0.71 | 0.84 | 1.05 |
| 11-10 16:09 | +10 | SOL | UP | 0.38 | 0.53 | 1.15 |
| 11-10 16:09 | +10 stop | SOL | UP | 0.43 | 0.53 | 0.64 |
| 11-10 16:08 | +10 stop | ZEC | DOWN | 0.47 | 0.59 | 0.85 |
| 11-10 16:08 | +10 | ZEC | DOWN | 0.47 | 0.59 | 0.85 |
| 11-10 16:08 | +5 | ZEC | DOWN | 0.47 | 0.59 | 0.85 |
| 11-10 16:08 | +5 | SOL | DOWN | 0.61 | 0.69 | 0.48 |
| 11-10 16:07 | +10 stop | BTC | DOWN | 0.59 | 0.21 | -4.09 |
| 11-10 16:07 | +10 stop | XRP | DOWN | 0.64 | 0.47 | -2.05 |
| 11-10 16:07 | +10 stop | NEAR | DOWN | 0.64 | 0.47 | -2.05 |
| 11-10 16:06 | +10 stop | DOGE | DOWN | 0.71 | 0.48 | -2.63 |
| 11-10 16:06 | +10 stop | SOL | DOWN | 0.71 | 0.50 | -2.43 |
| 11-10 16:06 | +5 | SOL | DOWN | 0.71 | 0.77 | 0.32 |
