# Range-Scalp Bot

*Updated Mon Oct 12 02:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12919 | 11152 | 1767 (25) | 1 | $-4266.27 | -5.2% |
| **+10¢** | 9795 | 7753 | 2042 (37) | 0 | $-3983.65 | -6.5% |
| **+15¢** | 8236 | 6059 | 2177 (55) | 4 | $-3480.91 | -6.7% |
| **+20¢** | 7337 | 5070 | 2267 (69) | 4 | $-2957.04 | -6.4% |
| **+10¢ (15¢ stop)** | 15924 | 15883 | 41 (25) | 0 | $-6273.48 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 02:37 | +5 | NEAR | DOWN | 0.63 | open |  |
| 10-12 02:35 | +10 stop | NEAR | DOWN | 0.52 | 0.65 | 0.96 |
| 10-12 02:35 | +10 | NEAR | DOWN | 0.52 | 0.65 | 0.96 |
| 10-12 02:35 | +5 | NEAR | DOWN | 0.52 | 0.57 | 0.14 |
| 10-12 02:35 | +10 stop | ZEC | UP | 0.64 | 0.81 | 1.42 |
| 10-12 02:35 | +10 | ZEC | UP | 0.64 | 0.81 | 1.42 |
| 10-12 02:35 | +5 | ZEC | UP | 0.64 | 0.81 | 1.42 |
| 10-12 02:35 | +10 stop | XRP | UP | 0.65 | 0.77 | 0.91 |
| 10-12 02:35 | +20 | XRP | UP | 0.65 | open |  |
| 10-12 02:35 | +15 | XRP | UP | 0.65 | open |  |
| 10-12 02:35 | +10 | XRP | UP | 0.65 | 0.77 | 0.91 |
| 10-12 02:35 | +5 | XRP | UP | 0.65 | 0.71 | 0.29 |
| 10-12 02:34 | +10 stop | SOL | UP | 0.67 | 0.77 | 0.71 |
| 10-12 02:34 | +20 | SOL | UP | 0.67 | open |  |
| 10-12 02:34 | +15 | SOL | UP | 0.67 | open |  |
| 10-12 02:34 | +10 | SOL | UP | 0.67 | 0.77 | 0.71 |
| 10-12 02:34 | +5 | SOL | UP | 0.67 | 0.77 | 0.71 |
| 10-12 02:31 | +10 stop | ZEC | UP | 0.67 | 0.77 | 0.71 |
| 10-12 02:31 | +20 | ZEC | UP | 0.67 | 0.89 | 1.97 |
| 10-12 02:31 | +15 | ZEC | UP | 0.68 | 0.84 | 1.34 |
| 10-12 02:31 | +10 | ZEC | UP | 0.67 | 0.77 | 0.71 |
| 10-12 02:31 | +5 | ZEC | UP | 0.67 | 0.74 | 0.40 |
| 10-12 02:31 | +10 stop | NEAR | DOWN | 0.64 | 0.75 | 0.79 |
| 10-12 02:31 | +20 | NEAR | DOWN | 0.64 | open |  |
| 10-12 02:31 | +15 | NEAR | DOWN | 0.64 | open |  |
| 10-12 02:31 | +10 | NEAR | DOWN | 0.64 | 0.75 | 0.79 |
| 10-12 02:31 | +5 | NEAR | DOWN | 0.64 | 0.72 | 0.48 |
| 10-12 02:31 | +10 stop | BTC | UP | 0.71 | 0.83 | 0.95 |
| 10-12 02:31 | +20 | BTC | UP | 0.71 | open |  |
| 10-12 02:31 | +15 | BTC | UP | 0.71 | open |  |
| 10-12 02:31 | +10 | BTC | UP | 0.71 | 0.83 | 0.95 |
| 10-12 02:31 | +5 | BTC | UP | 0.71 | 0.79 | 0.53 |
| 10-12 02:27 | +10 stop | XRP | DOWN | 0.56 | 0.67 | 0.76 |
| 10-12 02:26 | +10 stop | ZEC | DOWN | 0.71 | 0.48 | -2.63 |
| 10-12 02:26 | +5 | ZEC | DOWN | 0.71 | 0.77 | 0.32 |
| 10-12 02:26 | +10 stop | HYPE | UP | 0.66 | 0.47 | -2.24 |
| 10-12 02:25 | +10 stop | NEAR | DOWN | 0.46 | 0.30 | -1.88 |
| 10-12 02:25 | +10 stop | BNB | UP | 0.64 | 0.77 | 1.03 |
| 10-12 02:25 | +20 | BNB | UP | 0.64 | 0.87 | 2.08 |
| 10-12 02:25 | +15 | BNB | UP | 0.64 | 0.80 | 1.34 |
