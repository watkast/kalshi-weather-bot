# Range-Scalp Bot

*Updated Sun Oct 25 08:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32852 | 28653 | 4199 (42) | 2 | $-9293.27 | -4.5% |
| **+10¢** | 24591 | 19729 | 4862 (60) | 3 | $-8299.45 | -5.4% |
| **+15¢** | 20582 | 15349 | 5233 (83) | 3 | $-7472.41 | -5.8% |
| **+20¢** | 18234 | 12756 | 5478 (105) | 4 | $-6608.32 | -5.8% |
| **+10¢ (15¢ stop)** | 40336 | 40276 | 60 (32) | 0 | $-15404.61 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 08:24 | +10 stop | XRP | DOWN | 0.65 | 0.49 | -1.94 |
| 10-25 08:24 | +5 | XRP | DOWN | 0.65 | 0.80 | 1.22 |
| 10-25 08:24 | +10 stop | HYPE | UP | 0.63 | 0.77 | 1.10 |
| 10-25 08:23 | +10 stop | XRP | UP | 0.51 | 0.33 | -2.14 |
| 10-25 08:23 | +15 | XRP | UP | 0.51 | open |  |
| 10-25 08:23 | +10 | XRP | UP | 0.51 | open |  |
| 10-25 08:23 | +5 | XRP | UP | 0.51 | 0.57 | 0.24 |
| 10-25 08:23 | +10 stop | ZEC | DOWN | 0.67 | 0.81 | 1.13 |
| 10-25 08:21 | +10 stop | NEAR | DOWN | 0.58 | 0.73 | 1.18 |
| 10-25 08:21 | +10 stop | ETH | DOWN | 0.67 | 0.82 | 1.23 |
| 10-25 08:21 | +10 | ETH | DOWN | 0.67 | 0.82 | 1.23 |
| 10-25 08:21 | +5 | ETH | DOWN | 0.67 | 0.74 | 0.40 |
| 10-25 08:21 | +10 stop | ZEC | UP | 0.64 | 0.36 | -3.11 |
| 10-25 08:21 | +5 | DOGE | DOWN | 0.63 | 0.78 | 1.20 |
| 10-25 08:20 | +5 | SOL | DOWN | 0.56 | 0.66 | 0.66 |
| 10-25 08:19 | +10 stop | BNB | DOWN | 0.70 | 0.81 | 0.80 |
| 10-25 08:19 | +10 stop | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-25 08:19 | +5 | ZEC | DOWN | 0.68 | 0.81 | 1.03 |
| 10-25 08:19 | +10 stop | XRP | UP | 0.60 | 0.78 | 1.50 |
| 10-25 08:19 | +5 | NEAR | DOWN | 0.68 | 0.73 | 0.20 |
| 10-25 08:19 | +5 | DOGE | DOWN | 0.65 | 0.70 | 0.20 |
| 10-25 08:18 | +5 | SOL | DOWN | 0.63 | 0.72 | 0.58 |
| 10-25 08:18 | +10 stop | ZEC | DOWN | 0.63 | 0.48 | -1.85 |
| 10-25 08:18 | +15 | ZEC | DOWN | 0.63 | 0.81 | 1.52 |
| 10-25 08:18 | +10 | ZEC | DOWN | 0.63 | 0.81 | 1.52 |
| 10-25 08:18 | +5 | ZEC | DOWN | 0.63 | 0.68 | 0.17 |
| 10-25 08:18 | +5 | DOGE | DOWN | 0.60 | 0.67 | 0.37 |
| 10-25 08:18 | +10 stop | HYPE | DOWN | 0.59 | 0.38 | -2.44 |
| 10-25 08:18 | +10 | HYPE | DOWN | 0.59 | open |  |
| 10-25 08:18 | +5 | HYPE | DOWN | 0.59 | open |  |
| 10-25 08:18 | +10 stop | HYPE | DOWN | 0.54 | 0.65 | 0.76 |
| 10-25 08:18 | +20 | HYPE | DOWN | 0.54 | open |  |
| 10-25 08:18 | +15 | HYPE | DOWN | 0.54 | open |  |
| 10-25 08:18 | +10 | HYPE | DOWN | 0.54 | 0.65 | 0.76 |
| 10-25 08:18 | +5 | HYPE | DOWN | 0.54 | 0.65 | 0.76 |
| 10-25 08:18 | +10 stop | BNB | DOWN | 0.57 | 0.67 | 0.66 |
| 10-25 08:17 | +10 | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-25 08:17 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-25 08:17 | +10 stop | BTC | DOWN | 0.71 | 0.81 | 0.74 |
| 10-25 08:17 | +20 | BTC | DOWN | 0.71 | 0.92 | 1.86 |
