# Range-Scalp Bot

*Updated Tue Nov 17 23:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63256 | 55175 | 8081 (118) | 2 | $-17237.11 | -4.3% |
| **+10¢** | 47259 | 37803 | 9456 (159) | 3 | $-16123.60 | -5.4% |
| **+15¢** | 39619 | 29422 | 10197 (203) | 6 | $-14611.81 | -5.9% |
| **+20¢** | 35299 | 24598 | 10701 (258) | 6 | $-12857.11 | -5.8% |
| **+10¢ (15¢ stop)** | 76982 | 76824 | 158 (93) | 3 | $-28354.15 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 23:32 | +5 | NEAR | UP | 0.59 | 0.66 | 0.37 |
| 11-17 23:32 | +10 stop | XRP | UP | 0.49 | 0.60 | 0.75 |
| 11-17 23:32 | +20 | XRP | UP | 0.49 | open |  |
| 11-17 23:32 | +15 | XRP | UP | 0.49 | open |  |
| 11-17 23:32 | +10 | XRP | UP | 0.49 | 0.60 | 0.75 |
| 11-17 23:32 | +5 | XRP | UP | 0.49 | 0.60 | 0.75 |
| 11-17 23:32 | +10 stop | SOL | UP | 0.54 | open |  |
| 11-17 23:32 | +20 | SOL | UP | 0.54 | open |  |
| 11-17 23:32 | +15 | SOL | UP | 0.54 | open |  |
| 11-17 23:32 | +10 | SOL | UP | 0.54 | open |  |
| 11-17 23:32 | +5 | SOL | UP | 0.54 | open |  |
| 11-17 23:32 | +10 stop | NEAR | UP | 0.71 | open |  |
| 11-17 23:32 | +20 | NEAR | UP | 0.71 | open |  |
| 11-17 23:32 | +15 | NEAR | UP | 0.71 | open |  |
| 11-17 23:32 | +10 | NEAR | UP | 0.71 | open |  |
| 11-17 23:31 | +10 stop | BTC | DOWN | 0.62 | 0.76 | 1.10 |
| 11-17 23:31 | +20 | BTC | DOWN | 0.63 | open |  |
| 11-17 23:31 | +15 | BTC | DOWN | 0.63 | open |  |
| 11-17 23:31 | +10 | BTC | DOWN | 0.63 | 0.76 | 1.00 |
| 11-17 23:31 | +5 | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-17 23:31 | +10 stop | ZEC | DOWN | 0.53 | open |  |
| 11-17 23:31 | +20 | ZEC | DOWN | 0.53 | open |  |
| 11-17 23:31 | +15 | ZEC | DOWN | 0.54 | open |  |
| 11-17 23:31 | +10 | ZEC | DOWN | 0.54 | open |  |
| 11-17 23:31 | +5 | ZEC | DOWN | 0.54 | open |  |
| 11-17 23:31 | +10 stop | ETH | DOWN | 0.55 | 0.65 | 0.66 |
| 11-17 23:31 | +20 | ETH | DOWN | 0.55 | open |  |
| 11-17 23:31 | +15 | ETH | DOWN | 0.55 | open |  |
| 11-17 23:31 | +10 | ETH | DOWN | 0.55 | 0.65 | 0.66 |
| 11-17 23:31 | +5 | ETH | DOWN | 0.56 | 0.65 | 0.56 |
| 11-17 23:27 | +10 stop | XRP | UP | 0.46 | 0.60 | 1.05 |
| 11-17 23:27 | +10 stop | NEAR | DOWN | 0.64 | 0.79 | 1.20 |
| 11-17 23:27 | +20 | NEAR | DOWN | 0.64 | 0.93 | 2.72 |
| 11-17 23:27 | +15 | NEAR | DOWN | 0.64 | 0.79 | 1.24 |
| 11-17 23:27 | +10 | NEAR | DOWN | 0.64 | 0.79 | 1.24 |
| 11-17 23:27 | +5 | NEAR | DOWN | 0.64 | 0.79 | 1.24 |
| 11-17 23:25 | +10 stop | XRP | DOWN | 0.65 | 0.38 | -3.03 |
| 11-17 23:25 | +20 | XRP | DOWN | 0.65 | 0.90 | 2.27 |
| 11-17 23:25 | +15 | XRP | DOWN | 0.65 | 0.80 | 1.22 |
| 11-17 23:25 | +10 | XRP | DOWN | 0.65 | 0.80 | 1.22 |
