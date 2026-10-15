# Range-Scalp Bot

*Updated Thu Oct 15 00:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16836 | 14605 | 2231 (28) | 2 | $-5208.03 | -4.9% |
| **+10¢** | 12727 | 10140 | 2587 (40) | 3 | $-4753.75 | -5.9% |
| **+15¢** | 10690 | 7911 | 2779 (59) | 3 | $-4261.18 | -6.4% |
| **+20¢** | 9497 | 6586 | 2911 (76) | 4 | $-3758.84 | -6.3% |
| **+10¢ (15¢ stop)** | 20735 | 20685 | 50 (29) | 0 | $-8019.90 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 00:58 | +5 | BTC | UP | 0.71 | 0.82 | 0.84 |
| 10-15 00:57 | +10 stop | BTC | UP | 0.55 | 0.72 | 1.37 |
| 10-15 00:57 | +10 | BTC | UP | 0.55 | 0.72 | 1.37 |
| 10-15 00:57 | +5 | BTC | UP | 0.55 | 0.60 | 0.15 |
| 10-15 00:57 | +10 stop | ETH | DOWN | 0.60 | 0.86 | 2.34 |
| 10-15 00:56 | +10 stop | DOGE | DOWN | 0.68 | 0.48 | -2.34 |
| 10-15 00:56 | +10 stop | BNB | DOWN | 0.63 | 0.81 | 1.52 |
| 10-15 00:56 | +10 stop | BTC | DOWN | 0.33 | 0.64 | 2.77 |
| 10-15 00:55 | +10 stop | DOGE | DOWN | 0.70 | 0.55 | -1.83 |
| 10-15 00:55 | +20 | DOGE | DOWN | 0.70 | open |  |
| 10-15 00:55 | +15 | DOGE | DOWN | 0.70 | 0.86 | 1.36 |
| 10-15 00:55 | +10 | DOGE | DOWN | 0.70 | 0.86 | 1.36 |
| 10-15 00:55 | +5 | DOGE | DOWN | 0.71 | 0.77 | 0.32 |
| 10-15 00:55 | +5 | HYPE | DOWN | 0.58 | 0.77 | 1.59 |
| 10-15 00:55 | +10 stop | ZEC | UP | 0.66 | 0.50 | -1.94 |
| 10-15 00:55 | +20 | ZEC | UP | 0.66 | 0.89 | 2.07 |
| 10-15 00:55 | +15 | ZEC | UP | 0.66 | 0.89 | 2.07 |
| 10-15 00:55 | +10 | ZEC | UP | 0.66 | 0.79 | 1.02 |
| 10-15 00:55 | +5 | ZEC | UP | 0.66 | 0.79 | 1.03 |
| 10-15 00:54 | +10 stop | ETH | UP | 0.55 | 0.30 | -2.83 |
| 10-15 00:54 | +15 | ETH | UP | 0.55 | open |  |
| 10-15 00:54 | +10 | ETH | UP | 0.55 | open |  |
| 10-15 00:54 | +5 | ETH | UP | 0.55 | open |  |
| 10-15 00:54 | +10 stop | HYPE | UP | 0.48 | 0.19 | -3.19 |
| 10-15 00:54 | +20 | HYPE | UP | 0.48 | open |  |
| 10-15 00:54 | +15 | HYPE | UP | 0.48 | open |  |
| 10-15 00:54 | +10 | HYPE | UP | 0.48 | open |  |
| 10-15 00:54 | +5 | HYPE | UP | 0.48 | 0.57 | 0.54 |
| 10-15 00:54 | +10 stop | BNB | UP | 0.70 | 0.47 | -2.63 |
| 10-15 00:54 | +20 | BNB | UP | 0.70 | 0.94 | 2.26 |
| 10-15 00:54 | +15 | BNB | UP | 0.70 | 0.94 | 2.26 |
| 10-15 00:54 | +10 | BNB | UP | 0.70 | 0.94 | 2.26 |
| 10-15 00:54 | +5 | BNB | UP | 0.71 | 0.94 | 2.16 |
| 10-15 00:54 | +10 stop | BTC | UP | 0.64 | 0.42 | -2.55 |
| 10-15 00:54 | +20 | BTC | UP | 0.64 | 0.91 | 2.44 |
| 10-15 00:54 | +15 | BTC | UP | 0.64 | 0.82 | 1.52 |
| 10-15 00:54 | +10 | BTC | UP | 0.64 | 0.74 | 0.69 |
| 10-15 00:54 | +5 | BTC | UP | 0.64 | 0.74 | 0.69 |
| 10-15 00:53 | +10 stop | SOL | UP | 0.64 | 0.43 | -2.45 |
| 10-15 00:53 | +10 stop | DOGE | UP | 0.71 | 0.91 | 1.80 |
