# Range-Scalp Bot

*Updated Wed Oct 14 13:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16031 | 13889 | 2142 (27) | 5 | $-5056.83 | -5.0% |
| **+10¢** | 12129 | 9644 | 2485 (39) | 5 | $-4673.02 | -6.1% |
| **+15¢** | 10194 | 7525 | 2669 (58) | 6 | $-4194.61 | -6.6% |
| **+20¢** | 9064 | 6264 | 2800 (75) | 6 | $-3728.96 | -6.6% |
| **+10¢ (15¢ stop)** | 19738 | 19688 | 50 (29) | 2 | $-7609.65 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 13:24 | +10 stop | NEAR | UP | 0.69 | open |  |
| 10-14 13:24 | +10 | NEAR | UP | 0.69 | open |  |
| 10-14 13:24 | +5 | NEAR | UP | 0.69 | 0.76 | 0.42 |
| 10-14 13:24 | +10 stop | BTC | DOWN | 0.58 | 0.39 | -2.25 |
| 10-14 13:24 | +5 | BNB | DOWN | 0.66 | open |  |
| 10-14 13:24 | +5 | SOL | DOWN | 0.68 | open |  |
| 10-14 13:23 | +10 stop | SOL | DOWN | 0.60 | open |  |
| 10-14 13:23 | +20 | SOL | DOWN | 0.60 | open |  |
| 10-14 13:23 | +15 | SOL | DOWN | 0.60 | open |  |
| 10-14 13:23 | +10 | SOL | DOWN | 0.60 | open |  |
| 10-14 13:23 | +5 | SOL | DOWN | 0.60 | 0.65 | 0.17 |
| 10-14 13:23 | +10 stop | BNB | DOWN | 0.65 | 0.38 | -3.03 |
| 10-14 13:23 | +5 | BNB | DOWN | 0.65 | 0.70 | 0.19 |
| 10-14 13:22 | +10 stop | ZEC | DOWN | 0.56 | 0.25 | -3.42 |
| 10-14 13:22 | +10 stop | NEAR | UP | 0.61 | 0.71 | 0.68 |
| 10-14 13:21 | +10 stop | BTC | DOWN | 0.66 | 0.48 | -2.14 |
| 10-14 13:20 | +10 stop | NEAR | DOWN | 0.63 | 0.37 | -2.94 |
| 10-14 13:20 | +10 stop | ZEC | DOWN | 0.63 | 0.47 | -1.95 |
| 10-14 13:20 | +5 | ZEC | DOWN | 0.63 | open |  |
| 10-14 13:19 | +10 stop | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 10-14 13:19 | +10 stop | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 10-14 13:19 | +10 stop | XRP | DOWN | 0.69 | 0.79 | 0.73 |
| 10-14 13:19 | +10 stop | ETH | DOWN | 0.58 | 0.72 | 1.07 |
| 10-14 13:19 | +5 | BNB | DOWN | 0.69 | 0.76 | 0.42 |
| 10-14 13:19 | +5 | ETH | DOWN | 0.61 | 0.66 | 0.17 |
| 10-14 13:19 | +5 | SOL | DOWN | 0.71 | 0.76 | 0.22 |
| 10-14 13:19 | +10 stop | HYPE | DOWN | 0.70 | 0.81 | 0.84 |
| 10-14 13:18 | +10 stop | NEAR | UP | 0.57 | 0.39 | -2.15 |
| 10-14 13:18 | +10 | NEAR | UP | 0.58 | 0.71 | 0.97 |
| 10-14 13:18 | +5 | NEAR | UP | 0.59 | 0.64 | 0.16 |
| 10-14 13:18 | +10 | BNB | UP | 0.51 | 0.61 | 0.65 |
| 10-14 13:18 | +5 | ZEC | UP | 0.47 | 0.54 | 0.34 |
| 10-14 13:18 | +15 | BTC | UP | 0.53 | open |  |
| 10-14 13:18 | +5 | BNB | UP | 0.58 | 0.64 | 0.25 |
| 10-14 13:17 | +10 stop | BTC | UP | 0.64 | 0.46 | -2.15 |
| 10-14 13:17 | +10 | BTC | UP | 0.64 | open |  |
| 10-14 13:17 | +10 stop | BNB | UP | 0.55 | 0.38 | -2.05 |
| 10-14 13:17 | +20 | BNB | UP | 0.54 | open |  |
| 10-14 13:17 | +15 | BNB | UP | 0.54 | open |  |
| 10-14 13:17 | +10 | BNB | UP | 0.54 | 0.64 | 0.65 |
