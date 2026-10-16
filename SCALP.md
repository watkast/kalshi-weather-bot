# Range-Scalp Bot

*Updated Fri Oct 16 14:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19393 | 16857 | 2536 (29) | 4 | $-5804.40 | -4.8% |
| **+10¢** | 14621 | 11689 | 2932 (41) | 4 | $-5217.54 | -5.7% |
| **+15¢** | 12235 | 9078 | 3157 (60) | 4 | $-4743.68 | -6.2% |
| **+20¢** | 10851 | 7541 | 3310 (79) | 4 | $-4231.14 | -6.2% |
| **+10¢ (15¢ stop)** | 23852 | 23802 | 50 (29) | 0 | $-9159.58 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 14:43 | +10 stop | BNB | UP | 0.70 | 0.80 | 0.73 |
| 10-16 14:43 | +10 stop | BTC | DOWN | 0.33 | 0.59 | 2.28 |
| 10-16 14:43 | +10 | BTC | DOWN | 0.33 | 0.59 | 2.27 |
| 10-16 14:43 | +5 | BTC | DOWN | 0.31 | 0.59 | 2.48 |
| 10-16 14:43 | +10 stop | XRP | DOWN | 0.64 | 0.42 | -2.54 |
| 10-16 14:43 | +20 | XRP | DOWN | 0.64 | open |  |
| 10-16 14:43 | +10 stop | ETH | DOWN | 0.45 | 0.63 | 1.45 |
| 10-16 14:43 | +10 stop | BTC | DOWN | 0.45 | 0.65 | 1.66 |
| 10-16 14:43 | +10 | BTC | DOWN | 0.45 | 0.65 | 1.66 |
| 10-16 14:43 | +5 | BTC | DOWN | 0.45 | 0.65 | 1.66 |
| 10-16 14:42 | +10 | ZEC | UP | 0.63 | 0.74 | 0.79 |
| 10-16 14:42 | +10 stop | HYPE | DOWN | 0.68 | 0.47 | -2.44 |
| 10-16 14:42 | +20 | HYPE | DOWN | 0.69 | open |  |
| 10-16 14:42 | +15 | HYPE | DOWN | 0.69 | open |  |
| 10-16 14:42 | +10 | HYPE | DOWN | 0.67 | open |  |
| 10-16 14:42 | +5 | HYPE | DOWN | 0.67 | open |  |
| 10-16 14:41 | +10 | ZEC | DOWN | 0.41 | 0.59 | 1.47 |
| 10-16 14:41 | +10 stop | DOGE | DOWN | 0.66 | 0.29 | -4.01 |
| 10-16 14:41 | +10 | DOGE | DOWN | 0.66 | open |  |
| 10-16 14:41 | +5 | DOGE | DOWN | 0.66 | open |  |
| 10-16 14:41 | +10 stop | SOL | DOWN | 0.54 | 0.30 | -2.73 |
| 10-16 14:41 | +10 stop | ETH | DOWN | 0.62 | 0.72 | 0.68 |
| 10-16 14:41 | +10 stop | ZEC | DOWN | 0.59 | 0.42 | -2.05 |
| 10-16 14:40 | +10 stop | DOGE | UP | 0.45 | 0.55 | 0.64 |
| 10-16 14:40 | +20 | DOGE | UP | 0.45 | 0.69 | 2.07 |
| 10-16 14:40 | +15 | DOGE | UP | 0.45 | 0.69 | 2.07 |
| 10-16 14:40 | +10 | DOGE | UP | 0.45 | 0.55 | 0.64 |
| 10-16 14:40 | +5 | DOGE | UP | 0.45 | 0.55 | 0.64 |
| 10-16 14:40 | +10 stop | SOL | UP | 0.68 | 0.44 | -2.74 |
| 10-16 14:40 | +20 | SOL | UP | 0.69 | 0.92 | 2.13 |
| 10-16 14:40 | +15 | SOL | UP | 0.70 | 0.92 | 2.03 |
| 10-16 14:40 | +10 | SOL | UP | 0.70 | 0.83 | 1.05 |
| 10-16 14:40 | +5 | SOL | UP | 0.70 | 0.77 | 0.42 |
| 10-16 14:40 | +10 stop | BNB | UP | 0.49 | 0.67 | 1.46 |
| 10-16 14:40 | +20 | BNB | UP | 0.49 | 0.80 | 2.80 |
| 10-16 14:40 | +15 | BNB | UP | 0.48 | 0.67 | 1.56 |
| 10-16 14:40 | +10 | BNB | UP | 0.48 | 0.67 | 1.56 |
| 10-16 14:40 | +5 | BNB | UP | 0.49 | 0.67 | 1.46 |
| 10-16 14:40 | +10 stop | BTC | UP | 0.51 | 0.64 | 0.95 |
| 10-16 14:40 | +20 | BTC | UP | 0.50 | 0.70 | 1.67 |
