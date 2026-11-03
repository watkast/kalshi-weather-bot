# Range-Scalp Bot

*Updated Tue Nov 03 22:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46408 | 40407 | 6001 (72) | 2 | $-13370.59 | -4.6% |
| **+10¢** | 34648 | 27696 | 6952 (96) | 3 | $-12213.30 | -5.6% |
| **+15¢** | 29005 | 21530 | 7475 (124) | 5 | $-11147.96 | -6.1% |
| **+20¢** | 25769 | 17935 | 7834 (164) | 5 | $-9855.19 | -6.1% |
| **+10¢ (15¢ stop)** | 56606 | 56513 | 93 (56) | 0 | $-21216.63 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 22:25 | +10 stop | ZEC | DOWN | 0.56 | 0.38 | -2.15 |
| 11-03 22:25 | +5 | ZEC | DOWN | 0.55 | 0.62 | 0.35 |
| 11-03 22:25 | +10 stop | BTC | UP | 0.64 | 0.47 | -2.05 |
| 11-03 22:25 | +20 | BTC | UP | 0.65 | open |  |
| 11-03 22:25 | +15 | BTC | UP | 0.64 | open |  |
| 11-03 22:25 | +10 | BTC | UP | 0.64 | open |  |
| 11-03 22:25 | +5 | BTC | UP | 0.64 | open |  |
| 11-03 22:23 | +10 stop | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-03 22:23 | +15 | DOGE | DOWN | 0.68 | 0.84 | 1.34 |
| 11-03 22:23 | +10 | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-03 22:23 | +5 | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-03 22:22 | +10 stop | XRP | UP | 0.66 | 0.80 | 1.08 |
| 11-03 22:22 | +20 | XRP | UP | 0.66 | open |  |
| 11-03 22:22 | +15 | XRP | UP | 0.66 | open |  |
| 11-03 22:22 | +10 | XRP | UP | 0.66 | 0.80 | 1.08 |
| 11-03 22:22 | +5 | XRP | UP | 0.65 | 0.73 | 0.46 |
| 11-03 22:21 | +10 stop | ZEC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-03 22:21 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-03 22:21 | +10 stop | DOGE | UP | 0.54 | 0.36 | -2.15 |
| 11-03 22:21 | +10 stop | ETH | DOWN | 0.65 | 0.80 | 1.22 |
| 11-03 22:21 | +10 | ETH | DOWN | 0.65 | 0.80 | 1.22 |
| 11-03 22:21 | +5 | ETH | DOWN | 0.65 | 0.72 | 0.39 |
| 11-03 22:21 | +5 | BNB | UP | 0.54 | open |  |
| 11-03 22:21 | +10 stop | HYPE | UP | 0.19 | 0.66 | 4.43 |
| 11-03 22:21 | +20 | HYPE | UP | 0.18 | 0.66 | 4.52 |
| 11-03 22:21 | +15 | HYPE | UP | 0.18 | 0.66 | 4.52 |
| 11-03 22:21 | +10 | HYPE | UP | 0.18 | 0.66 | 4.52 |
| 11-03 22:21 | +5 | HYPE | UP | 0.19 | 0.66 | 4.43 |
| 11-03 22:20 | +10 stop | SOL | DOWN | 0.60 | 0.71 | 0.78 |
| 11-03 22:18 | +10 stop | SOL | UP | 0.68 | 0.43 | -2.84 |
| 11-03 22:17 | +10 stop | SOL | UP | 0.69 | 0.53 | -1.93 |
| 11-03 22:17 | +10 stop | BNB | UP | 0.70 | 0.55 | -1.83 |
| 11-03 22:17 | +20 | BNB | UP | 0.70 | open |  |
| 11-03 22:17 | +15 | BNB | UP | 0.70 | open |  |
| 11-03 22:17 | +10 | BNB | UP | 0.70 | open |  |
| 11-03 22:17 | +5 | BNB | UP | 0.70 | 0.77 | 0.42 |
| 11-03 22:17 | +10 stop | HYPE | UP | 0.57 | 0.70 | 0.97 |
| 11-03 22:17 | +20 | HYPE | UP | 0.57 | 0.80 | 2.00 |
| 11-03 22:17 | +15 | HYPE | UP | 0.57 | 0.80 | 2.00 |
| 11-03 22:17 | +10 | HYPE | UP | 0.57 | 0.70 | 0.97 |
