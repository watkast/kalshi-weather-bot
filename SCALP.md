# Range-Scalp Bot

*Updated Sun Oct 11 14:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12028 | 10379 | 1649 (24) | 1 | $-4006.05 | -5.3% |
| **+10¢** | 9128 | 7212 | 1916 (37) | 1 | $-3798.94 | -6.6% |
| **+15¢** | 7690 | 5656 | 2034 (54) | 1 | $-3243.90 | -6.7% |
| **+20¢** | 6855 | 4738 | 2117 (68) | 2 | $-2721.65 | -6.3% |
| **+10¢ (15¢ stop)** | 14810 | 14769 | 41 (25) | 1 | $-5879.79 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 14:12 | +10 stop | BTC | UP | 0.57 | open |  |
| 10-11 14:12 | +10 | BTC | UP | 0.63 | open |  |
| 10-11 14:12 | +5 | BTC | UP | 0.63 | open |  |
| 10-11 14:10 | +10 stop | HYPE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-11 14:09 | +5 | HYPE | DOWN | 0.64 | 0.78 | 1.10 |
| 10-11 14:09 | +10 stop | HYPE | DOWN | 0.55 | 0.65 | 0.66 |
| 10-11 14:09 | +5 | HYPE | DOWN | 0.55 | 0.61 | 0.25 |
| 10-11 14:08 | +10 stop | BTC | DOWN | 0.65 | 0.42 | -2.64 |
| 10-11 14:08 | +5 | BTC | DOWN | 0.65 | 0.70 | 0.19 |
| 10-11 14:06 | +10 stop | SOL | DOWN | 0.64 | 0.80 | 1.31 |
| 10-11 14:06 | +10 stop | HYPE | DOWN | 0.57 | 0.78 | 1.74 |
| 10-11 14:06 | +10 stop | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 10-11 14:06 | +20 | XRP | DOWN | 0.66 | 0.89 | 2.07 |
| 10-11 14:06 | +15 | XRP | DOWN | 0.65 | 0.85 | 1.75 |
| 10-11 14:06 | +10 | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 10-11 14:06 | +5 | XRP | DOWN | 0.65 | 0.74 | 0.60 |
| 10-11 14:05 | +10 stop | ZEC | UP | 0.56 | 0.38 | -2.15 |
| 10-11 14:05 | +10 stop | BNB | UP | 0.64 | 0.28 | -3.92 |
| 10-11 14:05 | +10 stop | BTC | UP | 0.57 | 0.30 | -3.03 |
| 10-11 14:04 | +10 stop | ZEC | DOWN | 0.57 | 0.40 | -2.05 |
| 10-11 14:04 | +20 | ZEC | DOWN | 0.57 | 0.81 | 2.11 |
| 10-11 14:04 | +15 | ZEC | DOWN | 0.57 | 0.81 | 2.11 |
| 10-11 14:04 | +10 | ZEC | DOWN | 0.57 | 0.81 | 2.11 |
| 10-11 14:04 | +5 | ZEC | DOWN | 0.57 | 0.81 | 2.11 |
| 10-11 14:04 | +10 stop | HYPE | DOWN | 0.70 | 0.49 | -2.47 |
| 10-11 14:04 | +20 | HYPE | DOWN | 0.70 | open |  |
| 10-11 14:04 | +15 | HYPE | DOWN | 0.70 | 0.87 | 1.43 |
| 10-11 14:04 | +10 | HYPE | DOWN | 0.70 | 0.87 | 1.43 |
| 10-11 14:04 | +5 | HYPE | DOWN | 0.70 | 0.78 | 0.48 |
| 10-11 14:01 | +10 stop | BNB | DOWN | 0.65 | 0.43 | -2.52 |
| 10-11 14:01 | +20 | BNB | DOWN | 0.65 | 0.87 | 1.98 |
| 10-11 14:01 | +15 | BNB | DOWN | 0.65 | 0.81 | 1.35 |
| 10-11 14:01 | +10 | BNB | DOWN | 0.65 | 0.75 | 0.72 |
| 10-11 14:01 | +5 | BNB | DOWN | 0.66 | 0.72 | 0.28 |
| 10-11 14:01 | +10 stop | SOL | DOWN | 0.69 | 0.50 | -2.23 |
| 10-11 14:01 | +20 | SOL | DOWN | 0.69 | 0.89 | 1.78 |
| 10-11 14:01 | +15 | SOL | DOWN | 0.69 | 0.85 | 1.36 |
| 10-11 14:01 | +10 | SOL | DOWN | 0.69 | 0.80 | 0.83 |
| 10-11 14:01 | +5 | SOL | DOWN | 0.69 | 0.80 | 0.83 |
| 10-11 14:01 | +10 stop | ETH | DOWN | 0.66 | 0.85 | 1.61 |
