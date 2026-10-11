# Range-Scalp Bot

*Updated Sun Oct 11 21:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12517 | 10803 | 1714 (25) | 2 | $-4144.81 | -5.2% |
| **+10¢** | 9498 | 7513 | 1985 (37) | 3 | $-3895.72 | -6.5% |
| **+15¢** | 7998 | 5887 | 2111 (55) | 3 | $-3345.23 | -6.7% |
| **+20¢** | 7129 | 4929 | 2200 (69) | 4 | $-2836.14 | -6.3% |
| **+10¢ (15¢ stop)** | 15420 | 15379 | 41 (25) | 0 | $-6050.61 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 21:04 | +10 stop | ETH | DOWN | 0.69 | 0.81 | 0.94 |
| 10-11 21:04 | +10 stop | BTC | UP | 0.50 | 0.30 | -2.33 |
| 10-11 21:04 | +5 | BNB | DOWN | 0.63 | 0.70 | 0.38 |
| 10-11 21:03 | +5 | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 10-11 21:03 | +5 | ZEC | DOWN | 0.63 | 0.71 | 0.48 |
| 10-11 21:02 | +10 stop | NEAR | UP | 0.60 | 0.45 | -1.85 |
| 10-11 21:02 | +20 | NEAR | UP | 0.60 | open |  |
| 10-11 21:02 | +15 | NEAR | UP | 0.60 | open |  |
| 10-11 21:02 | +10 | NEAR | UP | 0.60 | open |  |
| 10-11 21:02 | +5 | NEAR | UP | 0.60 | open |  |
| 10-11 21:02 | +5 | XRP | DOWN | 0.54 | 0.61 | 0.35 |
| 10-11 21:02 | +10 stop | XRP | DOWN | 0.60 | 0.71 | 0.78 |
| 10-11 21:02 | +20 | XRP | DOWN | 0.60 | 0.85 | 2.24 |
| 10-11 21:02 | +15 | XRP | DOWN | 0.60 | 0.79 | 1.61 |
| 10-11 21:02 | +10 | XRP | DOWN | 0.60 | 0.71 | 0.78 |
| 10-11 21:02 | +5 | XRP | DOWN | 0.60 | 0.65 | 0.17 |
| 10-11 21:02 | +5 | DOGE | DOWN | 0.64 | 0.73 | 0.59 |
| 10-11 21:01 | +10 stop | BTC | DOWN | 0.60 | 0.42 | -2.15 |
| 10-11 21:01 | +20 | BTC | DOWN | 0.60 | 0.81 | 1.82 |
| 10-11 21:01 | +15 | BTC | DOWN | 0.60 | 0.79 | 1.61 |
| 10-11 21:01 | +10 | BTC | DOWN | 0.60 | 0.79 | 1.61 |
| 10-11 21:01 | +5 | BTC | DOWN | 0.60 | 0.69 | 0.58 |
| 10-11 21:01 | +10 stop | ETH | DOWN | 0.60 | 0.34 | -2.93 |
| 10-11 21:01 | +20 | ETH | DOWN | 0.60 | 0.81 | 1.82 |
| 10-11 21:01 | +15 | ETH | DOWN | 0.60 | 0.81 | 1.82 |
| 10-11 21:01 | +10 | ETH | DOWN | 0.60 | 0.81 | 1.82 |
| 10-11 21:01 | +5 | ETH | DOWN | 0.60 | 0.68 | 0.47 |
| 10-11 21:01 | +10 stop | ZEC | DOWN | 0.60 | 0.71 | 0.78 |
| 10-11 21:01 | +20 | ZEC | DOWN | 0.60 | 0.85 | 2.24 |
| 10-11 21:01 | +15 | ZEC | DOWN | 0.60 | 0.78 | 1.50 |
| 10-11 21:01 | +10 | ZEC | DOWN | 0.60 | 0.71 | 0.78 |
| 10-11 21:01 | +5 | ZEC | DOWN | 0.60 | 0.66 | 0.27 |
| 10-11 21:01 | +10 stop | BNB | DOWN | 0.64 | 0.76 | 0.90 |
| 10-11 21:01 | +20 | BNB | DOWN | 0.64 | 0.89 | 2.26 |
| 10-11 21:01 | +15 | BNB | DOWN | 0.64 | 0.83 | 1.63 |
| 10-11 21:01 | +10 | BNB | DOWN | 0.64 | 0.76 | 0.90 |
| 10-11 21:01 | +5 | BNB | DOWN | 0.64 | 0.71 | 0.38 |
| 10-11 21:01 | +10 stop | SOL | DOWN | 0.69 | 0.80 | 0.83 |
| 10-11 21:01 | +20 | SOL | DOWN | 0.69 | open |  |
| 10-11 21:01 | +15 | SOL | DOWN | 0.69 | 0.87 | 1.57 |
