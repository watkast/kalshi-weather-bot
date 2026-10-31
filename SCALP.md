# Range-Scalp Bot

*Updated Sat Oct 31 20:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42685 | 37218 | 5467 (61) | 4 | $-12072.77 | -4.5% |
| **+10¢** | 31831 | 25506 | 6325 (83) | 3 | $-10846.94 | -5.4% |
| **+15¢** | 26629 | 19807 | 6822 (111) | 3 | $-9958.67 | -6.0% |
| **+20¢** | 23649 | 16500 | 7149 (143) | 5 | $-8835.40 | -6.0% |
| **+10¢ (15¢ stop)** | 52080 | 51997 | 83 (48) | 0 | $-19703.70 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 20:26 | +10 stop | XRP | UP | 0.59 | 0.71 | 0.92 |
| 10-31 20:26 | +20 | XRP | UP | 0.58 | open |  |
| 10-31 20:26 | +15 | XRP | UP | 0.59 | 0.74 | 1.23 |
| 10-31 20:26 | +10 | XRP | UP | 0.59 | 0.71 | 0.92 |
| 10-31 20:26 | +5 | XRP | UP | 0.59 | 0.71 | 0.92 |
| 10-31 20:25 | +10 stop | NEAR | UP | 0.48 | 0.31 | -2.03 |
| 10-31 20:25 | +5 | XRP | UP | 0.56 | 0.75 | 1.58 |
| 10-31 20:24 | +10 stop | HYPE | UP | 0.65 | 0.84 | 1.64 |
| 10-31 20:24 | +20 | HYPE | UP | 0.65 | 0.86 | 1.85 |
| 10-31 20:24 | +15 | HYPE | UP | 0.65 | 0.84 | 1.64 |
| 10-31 20:24 | +10 | HYPE | UP | 0.65 | 0.84 | 1.64 |
| 10-31 20:24 | +5 | HYPE | UP | 0.65 | 0.71 | 0.29 |
| 10-31 20:24 | +5 | SOL | UP | 0.66 | 0.71 | 0.19 |
| 10-31 20:23 | +10 stop | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 10-31 20:23 | +10 stop | XRP | UP | 0.50 | 0.75 | 2.18 |
| 10-31 20:23 | +20 | XRP | UP | 0.50 | 0.75 | 2.18 |
| 10-31 20:23 | +15 | XRP | UP | 0.50 | 0.75 | 2.18 |
| 10-31 20:23 | +10 | XRP | UP | 0.50 | 0.75 | 2.18 |
| 10-31 20:23 | +5 | XRP | UP | 0.50 | 0.59 | 0.55 |
| 10-31 20:22 | +15 | SOL | UP | 0.66 | 0.82 | 1.33 |
| 10-31 20:22 | +10 | SOL | UP | 0.66 | 0.82 | 1.33 |
| 10-31 20:22 | +5 | SOL | UP | 0.66 | 0.72 | 0.29 |
| 10-31 20:22 | +10 stop | NEAR | DOWN | 0.62 | 0.43 | -2.25 |
| 10-31 20:22 | +5 | BTC | UP | 0.53 | open |  |
| 10-31 20:21 | +10 stop | DOGE | UP | 0.58 | 0.25 | -3.62 |
| 10-31 20:21 | +15 | DOGE | UP | 0.58 | open |  |
| 10-31 20:21 | +10 | DOGE | UP | 0.58 | open |  |
| 10-31 20:21 | +5 | DOGE | UP | 0.58 | open |  |
| 10-31 20:21 | +10 stop | SOL | UP | 0.70 | 0.82 | 0.94 |
| 10-31 20:21 | +20 | SOL | UP | 0.70 | open |  |
| 10-31 20:21 | +10 stop | BTC | UP | 0.56 | 0.37 | -2.25 |
| 10-31 20:21 | +15 | BTC | UP | 0.56 | open |  |
| 10-31 20:21 | +10 | BTC | UP | 0.56 | open |  |
| 10-31 20:21 | +5 | BTC | UP | 0.57 | 0.62 | 0.15 |
| 10-31 20:20 | +5 | ETH | DOWN | 0.55 | 0.70 | 1.17 |
| 10-31 20:18 | +10 stop | BNB | DOWN | 0.64 | 0.77 | 1.00 |
| 10-31 20:18 | +20 | BNB | DOWN | 0.64 | 0.86 | 1.94 |
| 10-31 20:18 | +15 | BNB | DOWN | 0.64 | 0.86 | 1.94 |
| 10-31 20:18 | +10 | BNB | DOWN | 0.64 | 0.77 | 1.00 |
| 10-31 20:18 | +5 | BNB | DOWN | 0.64 | 0.77 | 1.00 |
