# Range-Scalp Bot

*Updated Mon Oct 26 07:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 34456 | 30072 | 4384 (43) | 2 | $-9607.98 | -4.4% |
| **+10¢** | 25796 | 20727 | 5069 (65) | 4 | $-8435.87 | -5.2% |
| **+15¢** | 21572 | 16116 | 5456 (89) | 5 | $-7559.38 | -5.6% |
| **+20¢** | 19116 | 13397 | 5719 (112) | 6 | $-6683.49 | -5.6% |
| **+10¢ (15¢ stop)** | 42228 | 42166 | 62 (33) | 0 | $-16093.49 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 07:25 | +10 stop | ZEC | UP | 0.36 | 0.57 | 1.75 |
| 10-26 07:25 | +10 stop | BTC | DOWN | 0.61 | 0.74 | 0.99 |
| 10-26 07:25 | +10 stop | ETH | UP | 0.62 | 0.44 | -2.15 |
| 10-26 07:25 | +10 stop | SOL | UP | 0.62 | 0.33 | -3.23 |
| 10-26 07:24 | +10 stop | DOGE | UP | 0.57 | 0.39 | -2.15 |
| 10-26 07:24 | +5 | DOGE | UP | 0.57 | open |  |
| 10-26 07:24 | +10 stop | ZEC | DOWN | 0.55 | 0.37 | -2.15 |
| 10-26 07:22 | +10 stop | ZEC | UP | 0.59 | 0.42 | -2.05 |
| 10-26 07:21 | +10 stop | ETH | UP | 0.50 | 0.64 | 1.05 |
| 10-26 07:21 | +10 stop | DOGE | UP | 0.57 | 0.70 | 0.97 |
| 10-26 07:21 | +10 stop | SOL | UP | 0.54 | 0.74 | 1.68 |
| 10-26 07:21 | +10 stop | BTC | DOWN | 0.62 | 0.44 | -2.15 |
| 10-26 07:21 | +15 | BTC | DOWN | 0.62 | open |  |
| 10-26 07:21 | +10 | BTC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-26 07:21 | +5 | ETH | DOWN | 0.63 | open |  |
| 10-26 07:21 | +10 | DOGE | DOWN | 0.60 | open |  |
| 10-26 07:21 | +10 stop | ZEC | DOWN | 0.63 | 0.46 | -2.05 |
| 10-26 07:21 | +5 | ZEC | DOWN | 0.63 | 0.68 | 0.17 |
| 10-26 07:20 | +10 stop | NEAR | DOWN | 0.57 | 0.68 | 0.76 |
| 10-26 07:20 | +15 | NEAR | DOWN | 0.57 | 0.78 | 1.79 |
| 10-26 07:20 | +10 | NEAR | DOWN | 0.57 | 0.68 | 0.76 |
| 10-26 07:20 | +5 | NEAR | DOWN | 0.57 | 0.68 | 0.76 |
| 10-26 07:20 | +5 | SOL | DOWN | 0.58 | 0.65 | 0.36 |
| 10-26 07:20 | +10 stop | XRP | DOWN | 0.69 | 0.83 | 1.15 |
| 10-26 07:20 | +5 | XRP | DOWN | 0.69 | 0.74 | 0.21 |
| 10-26 07:20 | +10 stop | ETH | DOWN | 0.62 | 0.39 | -2.64 |
| 10-26 07:20 | +10 stop | SOL | DOWN | 0.63 | 0.45 | -2.15 |
| 10-26 07:20 | +5 | BTC | DOWN | 0.67 | 0.74 | 0.40 |
| 10-26 07:19 | +10 stop | BNB | UP | 0.57 | 0.73 | 1.28 |
| 10-26 07:19 | +20 | BNB | UP | 0.57 | 0.78 | 1.79 |
| 10-26 07:19 | +15 | BNB | UP | 0.57 | 0.73 | 1.28 |
| 10-26 07:19 | +10 | BNB | UP | 0.57 | 0.73 | 1.28 |
| 10-26 07:19 | +5 | BNB | UP | 0.57 | 0.73 | 1.28 |
| 10-26 07:19 | +10 stop | DOGE | DOWN | 0.63 | 0.40 | -2.64 |
| 10-26 07:19 | +10 stop | SOL | UP | 0.58 | 0.41 | -2.05 |
| 10-26 07:19 | +10 stop | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 10-26 07:19 | +15 | HYPE | DOWN | 0.71 | 0.87 | 1.37 |
| 10-26 07:19 | +10 | HYPE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-26 07:19 | +5 | HYPE | DOWN | 0.71 | 0.79 | 0.53 |
| 10-26 07:18 | +10 stop | ETH | UP | 0.62 | 0.42 | -2.35 |
