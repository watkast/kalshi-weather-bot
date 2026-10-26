# Range-Scalp Bot

*Updated Mon Oct 26 14:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 34983 | 30546 | 4437 (43) | 8 | $-9677.24 | -4.4% |
| **+10¢** | 26174 | 21042 | 5132 (65) | 8 | $-8481.78 | -5.1% |
| **+15¢** | 21903 | 16378 | 5525 (89) | 9 | $-7585.24 | -5.5% |
| **+20¢** | 19414 | 13622 | 5792 (112) | 9 | $-6672.58 | -5.5% |
| **+10¢ (15¢ stop)** | 42822 | 42760 | 62 (33) | 0 | $-16214.15 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 14:53 | +10 stop | ETH | UP | 0.66 | 0.76 | 0.71 |
| 10-26 14:53 | +10 stop | ZEC | UP | 0.65 | 0.86 | 1.85 |
| 10-26 14:52 | +5 | SOL | UP | 0.71 | 0.78 | 0.42 |
| 10-26 14:52 | +10 stop | NEAR | UP | 0.60 | 0.71 | 0.78 |
| 10-26 14:52 | +10 stop | SOL | UP | 0.71 | 0.87 | 1.37 |
| 10-26 14:51 | +10 stop | ETH | DOWN | 0.58 | 0.42 | -1.96 |
| 10-26 14:51 | +5 | ETH | DOWN | 0.58 | open |  |
| 10-26 14:51 | +10 stop | ZEC | UP | 0.56 | 0.72 | 1.27 |
| 10-26 14:51 | +10 stop | DOGE | UP | 0.52 | 0.65 | 0.96 |
| 10-26 14:51 | +10 stop | HYPE | UP | 0.64 | 0.77 | 1.00 |
| 10-26 14:51 | +10 stop | NEAR | UP | 0.55 | 0.71 | 1.27 |
| 10-26 14:51 | +10 stop | XRP | UP | 0.54 | 0.70 | 1.27 |
| 10-26 14:51 | +10 stop | ETH | UP | 0.46 | 0.59 | 0.95 |
| 10-26 14:51 | +5 | ETH | UP | 0.45 | 0.59 | 1.03 |
| 10-26 14:49 | +10 stop | HYPE | UP | 0.65 | 0.78 | 1.01 |
| 10-26 14:49 | +10 stop | DOGE | UP | 0.66 | 0.80 | 1.12 |
| 10-26 14:48 | +10 stop | ETH | UP | 0.68 | 0.78 | 0.71 |
| 10-26 14:48 | +5 | ETH | UP | 0.68 | 0.78 | 0.71 |
| 10-26 14:48 | +10 stop | SOL | UP | 0.66 | 0.45 | -2.44 |
| 10-26 14:48 | +10 | SOL | UP | 0.66 | 0.78 | 0.91 |
| 10-26 14:48 | +5 | SOL | UP | 0.66 | 0.71 | 0.19 |
| 10-26 14:48 | +10 stop | NEAR | UP | 0.71 | 0.81 | 0.74 |
| 10-26 14:48 | +10 stop | XRP | UP | 0.69 | 0.79 | 0.73 |
| 10-26 14:48 | +10 stop | ZEC | UP | 0.66 | 0.77 | 0.81 |
| 10-26 14:46 | +10 stop | SOL | DOWN | 0.63 | 0.73 | 0.69 |
| 10-26 14:46 | +20 | SOL | DOWN | 0.63 | open |  |
| 10-26 14:46 | +15 | SOL | DOWN | 0.63 | open |  |
| 10-26 14:46 | +10 | SOL | DOWN | 0.63 | 0.73 | 0.69 |
| 10-26 14:46 | +5 | SOL | DOWN | 0.63 | 0.73 | 0.69 |
| 10-26 14:46 | +10 stop | DOGE | DOWN | 0.68 | 0.48 | -2.34 |
| 10-26 14:46 | +20 | DOGE | DOWN | 0.68 | open |  |
| 10-26 14:46 | +15 | DOGE | DOWN | 0.68 | open |  |
| 10-26 14:46 | +10 | DOGE | DOWN | 0.68 | open |  |
| 10-26 14:46 | +5 | DOGE | DOWN | 0.68 | open |  |
| 10-26 14:46 | +10 stop | BTC | DOWN | 0.70 | 0.50 | -2.33 |
| 10-26 14:46 | +20 | BTC | DOWN | 0.70 | open |  |
| 10-26 14:46 | +15 | BTC | DOWN | 0.70 | open |  |
| 10-26 14:46 | +10 | BTC | DOWN | 0.70 | open |  |
| 10-26 14:46 | +5 | BTC | DOWN | 0.70 | open |  |
| 10-26 14:46 | +10 stop | HYPE | DOWN | 0.66 | 0.46 | -2.34 |
