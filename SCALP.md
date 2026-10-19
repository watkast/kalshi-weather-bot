# Range-Scalp Bot

*Updated Mon Oct 19 20:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24541 | 21361 | 3180 (31) | 3 | $-7186.68 | -4.6% |
| **+10¢** | 18448 | 14777 | 3671 (46) | 4 | $-6395.24 | -5.5% |
| **+15¢** | 15447 | 11494 | 3953 (69) | 3 | $-5761.27 | -5.9% |
| **+20¢** | 13667 | 9527 | 4140 (87) | 3 | $-5173.33 | -6.0% |
| **+10¢ (15¢ stop)** | 30175 | 30123 | 52 (30) | 0 | $-11397.15 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 20:42 | +10 stop | BTC | DOWN | 0.59 | 0.41 | -2.14 |
| 10-19 20:41 | +10 stop | BTC | UP | 0.43 | 0.54 | 0.74 |
| 10-19 20:40 | +15 | SOL | UP | 0.70 | 0.90 | 1.80 |
| 10-19 20:40 | +10 stop | HYPE | UP | 0.66 | 0.78 | 0.91 |
| 10-19 20:39 | +5 | BTC | DOWN | 0.64 | open |  |
| 10-19 20:38 | +10 stop | BTC | DOWN | 0.62 | 0.47 | -1.85 |
| 10-19 20:37 | +10 stop | SOL | UP | 0.67 | 0.82 | 1.23 |
| 10-19 20:37 | +10 stop | ZEC | DOWN | 0.66 | 0.84 | 1.54 |
| 10-19 20:37 | +5 | ZEC | DOWN | 0.66 | 0.73 | 0.40 |
| 10-19 20:37 | +10 stop | XRP | DOWN | 0.69 | 0.82 | 1.04 |
| 10-19 20:37 | +10 | XRP | DOWN | 0.69 | 0.82 | 1.04 |
| 10-19 20:37 | +5 | XRP | DOWN | 0.69 | 0.78 | 0.62 |
| 10-19 20:37 | +10 stop | DOGE | DOWN | 0.55 | 0.65 | 0.66 |
| 10-19 20:37 | +5 | ETH | UP | 0.70 | 0.77 | 0.42 |
| 10-19 20:37 | +10 stop | HYPE | DOWN | 0.63 | 0.43 | -2.39 |
| 10-19 20:37 | +20 | HYPE | DOWN | 0.64 | open |  |
| 10-19 20:37 | +15 | HYPE | DOWN | 0.64 | open |  |
| 10-19 20:35 | +5 | ZEC | DOWN | 0.59 | 0.66 | 0.37 |
| 10-19 20:35 | +10 stop | BNB | DOWN | 0.62 | 0.73 | 0.75 |
| 10-19 20:35 | +10 | BNB | DOWN | 0.62 | 0.73 | 0.75 |
| 10-19 20:35 | +5 | BNB | DOWN | 0.62 | 0.69 | 0.34 |
| 10-19 20:35 | +10 stop | ETH | UP | 0.64 | 0.77 | 1.00 |
| 10-19 20:35 | +20 | ETH | UP | 0.64 | 0.89 | 2.26 |
| 10-19 20:35 | +15 | ETH | UP | 0.64 | 0.79 | 1.21 |
| 10-19 20:35 | +10 | ETH | UP | 0.64 | 0.77 | 1.00 |
| 10-19 20:35 | +5 | ETH | UP | 0.64 | 0.73 | 0.59 |
| 10-19 20:35 | +10 stop | XRP | DOWN | 0.57 | 0.70 | 0.97 |
| 10-19 20:35 | +10 stop | DOGE | DOWN | 0.47 | 0.57 | 0.64 |
| 10-19 20:35 | +10 stop | SOL | UP | 0.53 | 0.63 | 0.65 |
| 10-19 20:35 | +20 | SOL | UP | 0.53 | 0.82 | 2.61 |
| 10-19 20:35 | +15 | SOL | UP | 0.53 | 0.68 | 1.16 |
| 10-19 20:35 | +5 | ZEC | UP | 0.47 | 0.54 | 0.34 |
| 10-19 20:34 | +10 stop | ZEC | UP | 0.53 | 0.33 | -2.34 |
| 10-19 20:34 | +10 stop | XRP | UP | 0.41 | 0.60 | 1.56 |
| 10-19 20:34 | +10 stop | BTC | UP | 0.67 | 0.50 | -2.04 |
| 10-19 20:34 | +10 stop | DOGE | UP | 0.64 | 0.43 | -2.45 |
| 10-19 20:34 | +10 stop | BNB | DOWN | 0.57 | 0.69 | 0.86 |
| 10-19 20:34 | +20 | BNB | DOWN | 0.57 | 0.83 | 2.31 |
| 10-19 20:34 | +15 | BNB | DOWN | 0.57 | 0.73 | 1.27 |
| 10-19 20:34 | +10 | BNB | DOWN | 0.57 | 0.69 | 0.86 |
