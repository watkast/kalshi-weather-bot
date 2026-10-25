# Range-Scalp Bot

*Updated Sun Oct 25 12:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33126 | 28908 | 4218 (42) | 2 | $-9259.44 | -4.4% |
| **+10¢** | 24793 | 19910 | 4883 (60) | 3 | $-8226.25 | -5.3% |
| **+15¢** | 20750 | 15493 | 5257 (83) | 4 | $-7393.85 | -5.7% |
| **+20¢** | 18383 | 12879 | 5504 (105) | 5 | $-6505.39 | -5.6% |
| **+10¢ (15¢ stop)** | 40635 | 40575 | 60 (32) | 0 | $-15495.80 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 12:24 | +10 stop | XRP | UP | 0.55 | 0.34 | -2.44 |
| 10-25 12:24 | +20 | XRP | UP | 0.55 | open |  |
| 10-25 12:24 | +15 | XRP | UP | 0.55 | open |  |
| 10-25 12:24 | +10 | XRP | UP | 0.55 | open |  |
| 10-25 12:24 | +5 | XRP | UP | 0.55 | 0.60 | 0.15 |
| 10-25 12:24 | +10 stop | SOL | DOWN | 0.68 | 0.89 | 1.87 |
| 10-25 12:24 | +10 | SOL | DOWN | 0.68 | 0.89 | 1.87 |
| 10-25 12:24 | +10 stop | DOGE | DOWN | 0.57 | 0.77 | 1.69 |
| 10-25 12:24 | +20 | DOGE | DOWN | 0.58 | 0.86 | 2.57 |
| 10-25 12:24 | +15 | DOGE | DOWN | 0.58 | 0.77 | 1.63 |
| 10-25 12:24 | +10 | DOGE | DOWN | 0.58 | 0.77 | 1.62 |
| 10-25 12:24 | +5 | DOGE | DOWN | 0.58 | 0.77 | 1.60 |
| 10-25 12:24 | +10 stop | ETH | UP | 0.46 | 0.62 | 1.25 |
| 10-25 12:24 | +15 | ETH | UP | 0.45 | 0.62 | 1.35 |
| 10-25 12:24 | +10 | ETH | UP | 0.45 | 0.62 | 1.35 |
| 10-25 12:24 | +5 | ETH | UP | 0.45 | 0.62 | 1.32 |
| 10-25 12:23 | +10 stop | SOL | UP | 0.70 | 0.51 | -2.23 |
| 10-25 12:23 | +5 | SOL | UP | 0.70 | open |  |
| 10-25 12:22 | +10 stop | NEAR | DOWN | 0.66 | 0.36 | -3.33 |
| 10-25 12:21 | +10 stop | BNB | UP | 0.56 | 0.36 | -2.35 |
| 10-25 12:21 | +10 | BNB | UP | 0.56 | open |  |
| 10-25 12:21 | +5 | BNB | UP | 0.65 | open |  |
| 10-25 12:20 | +10 stop | ETH | DOWN | 0.60 | 0.42 | -2.15 |
| 10-25 12:20 | +10 stop | HYPE | UP | 0.64 | 0.79 | 1.21 |
| 10-25 12:20 | +10 | HYPE | UP | 0.64 | 0.79 | 1.21 |
| 10-25 12:20 | +5 | HYPE | UP | 0.64 | 0.79 | 1.21 |
| 10-25 12:18 | +10 stop | BNB | UP | 0.53 | 0.66 | 0.96 |
| 10-25 12:18 | +20 | BNB | UP | 0.53 | open |  |
| 10-25 12:18 | +15 | BNB | UP | 0.53 | open |  |
| 10-25 12:18 | +10 | BNB | UP | 0.53 | 0.66 | 0.96 |
| 10-25 12:18 | +5 | BNB | UP | 0.53 | 0.58 | 0.14 |
| 10-25 12:18 | +5 | HYPE | UP | 0.62 | 0.68 | 0.23 |
| 10-25 12:18 | +5 | ETH | UP | 0.65 | 0.72 | 0.39 |
| 10-25 12:17 | +10 stop | SOL | DOWN | 0.59 | 0.34 | -2.83 |
| 10-25 12:17 | +10 stop | BTC | DOWN | 0.60 | 0.73 | 0.99 |
| 10-25 12:17 | +20 | BTC | DOWN | 0.60 | 0.83 | 2.03 |
| 10-25 12:17 | +15 | BTC | DOWN | 0.60 | 0.77 | 1.40 |
| 10-25 12:17 | +10 | BTC | DOWN | 0.60 | 0.73 | 0.99 |
| 10-25 12:17 | +5 | BTC | DOWN | 0.58 | 0.68 | 0.66 |
| 10-25 12:16 | +10 stop | NEAR | DOWN | 0.65 | 0.40 | -2.83 |
