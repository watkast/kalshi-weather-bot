# Range-Scalp Bot

*Updated Wed Nov 04 04:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46810 | 40765 | 6045 (72) | 3 | $-13445.13 | -4.6% |
| **+10¢** | 34968 | 27960 | 7008 (96) | 3 | $-12263.73 | -5.6% |
| **+15¢** | 29283 | 21742 | 7541 (124) | 3 | $-11211.50 | -6.1% |
| **+20¢** | 26015 | 18117 | 7898 (164) | 3 | $-9862.89 | -6.0% |
| **+10¢ (15¢ stop)** | 57070 | 56977 | 93 (56) | 0 | $-21320.57 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 04:32 | +10 stop | BNB | DOWN | 0.63 | 0.76 | 1.00 |
| 11-04 04:32 | +10 stop | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-04 04:32 | +10 stop | XRP | DOWN | 0.62 | 0.74 | 0.89 |
| 11-04 04:31 | +10 stop | ETH | DOWN | 0.67 | 0.80 | 1.02 |
| 11-04 04:31 | +20 | ETH | DOWN | 0.67 | 0.87 | 1.76 |
| 11-04 04:31 | +15 | ETH | DOWN | 0.67 | 0.86 | 1.65 |
| 11-04 04:31 | +10 | ETH | DOWN | 0.67 | 0.80 | 1.02 |
| 11-04 04:31 | +5 | ETH | DOWN | 0.67 | 0.76 | 0.61 |
| 11-04 04:31 | +10 stop | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-04 04:31 | +20 | BTC | DOWN | 0.67 | 0.87 | 1.76 |
| 11-04 04:31 | +15 | BTC | DOWN | 0.67 | 0.84 | 1.44 |
| 11-04 04:31 | +10 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-04 04:31 | +5 | BTC | DOWN | 0.67 | 0.72 | 0.19 |
| 11-04 04:31 | +10 stop | HYPE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-04 04:31 | +20 | HYPE | DOWN | 0.64 | 0.84 | 1.73 |
| 11-04 04:31 | +15 | HYPE | DOWN | 0.64 | 0.80 | 1.31 |
| 11-04 04:31 | +10 | HYPE | DOWN | 0.64 | 0.76 | 0.90 |
| 11-04 04:31 | +5 | HYPE | DOWN | 0.64 | 0.69 | 0.18 |
| 11-04 04:31 | +10 stop | DOGE | DOWN | 0.69 | 0.81 | 0.92 |
| 11-04 04:31 | +20 | DOGE | DOWN | 0.69 | 0.90 | 1.88 |
| 11-04 04:31 | +15 | DOGE | DOWN | 0.69 | 0.87 | 1.55 |
| 11-04 04:31 | +10 | DOGE | DOWN | 0.68 | 0.81 | 1.03 |
| 11-04 04:31 | +5 | DOGE | DOWN | 0.68 | 0.74 | 0.30 |
| 11-04 04:31 | +10 stop | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 11-04 04:31 | +20 | SOL | DOWN | 0.66 | 0.87 | 1.86 |
| 11-04 04:31 | +15 | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 11-04 04:31 | +10 | SOL | DOWN | 0.66 | 0.77 | 0.81 |
| 11-04 04:31 | +5 | SOL | DOWN | 0.66 | 0.72 | 0.29 |
| 11-04 04:31 | +10 stop | BNB | UP | 0.59 | 0.37 | -2.54 |
| 11-04 04:31 | +20 | BNB | UP | 0.59 | open |  |
| 11-04 04:31 | +15 | BNB | UP | 0.59 | open |  |
| 11-04 04:31 | +10 | BNB | UP | 0.59 | open |  |
| 11-04 04:31 | +5 | BNB | UP | 0.59 | open |  |
| 11-04 04:31 | +10 stop | ZEC | UP | 0.52 | 0.35 | -2.04 |
| 11-04 04:31 | +20 | ZEC | UP | 0.52 | open |  |
| 11-04 04:31 | +15 | ZEC | UP | 0.53 | open |  |
| 11-04 04:31 | +10 | ZEC | UP | 0.53 | open |  |
| 11-04 04:31 | +5 | ZEC | UP | 0.53 | open |  |
| 11-04 04:31 | +10 stop | XRP | UP | 0.59 | 0.41 | -2.14 |
| 11-04 04:31 | +20 | XRP | UP | 0.59 | open |  |
