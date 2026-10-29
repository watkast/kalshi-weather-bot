# Range-Scalp Bot

*Updated Thu Oct 29 11:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39221 | 34224 | 4997 (49) | 1 | $-11022.92 | -4.5% |
| **+10¢** | 29252 | 23484 | 5768 (71) | 1 | $-9751.17 | -5.3% |
| **+15¢** | 24458 | 18261 | 6197 (98) | 1 | $-8722.63 | -5.7% |
| **+20¢** | 21697 | 15206 | 6491 (127) | 1 | $-7610.64 | -5.6% |
| **+10¢ (15¢ stop)** | 47938 | 47871 | 67 (35) | 0 | $-18206.10 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 11:42 | +10 stop | BNB | DOWN | 0.55 | 0.09 | -4.84 |
| 10-29 11:42 | +20 | BNB | DOWN | 0.55 | yes | -5.68 |
| 10-29 11:42 | +15 | BNB | DOWN | 0.55 | yes | -5.68 |
| 10-29 11:42 | +10 | BNB | DOWN | 0.55 | yes | -5.68 |
| 10-29 11:42 | +5 | BNB | DOWN | 0.55 | yes | -5.68 |
| 10-29 11:41 | +10 stop | SOL | UP | 0.66 | 0.92 | 2.35 |
| 10-29 11:41 | +10 | SOL | UP | 0.65 | 0.92 | 2.45 |
| 10-29 11:41 | +5 | SOL | UP | 0.65 | 0.92 | 2.45 |
| 10-29 11:41 | +5 | BTC | DOWN | 0.71 | yes | -7.25 |
| 10-29 11:40 | +10 stop | SOL | UP | 0.52 | 0.65 | 0.96 |
| 10-29 11:40 | +20 | SOL | UP | 0.52 | 0.92 | 3.73 |
| 10-29 11:40 | +15 | SOL | UP | 0.52 | 0.68 | 1.26 |
| 10-29 11:40 | +10 | SOL | UP | 0.52 | 0.65 | 0.96 |
| 10-29 11:40 | +5 | SOL | UP | 0.52 | 0.65 | 0.96 |
| 10-29 11:39 | +5 | BTC | DOWN | 0.71 | 0.77 | 0.32 |
| 10-29 11:39 | +10 stop | BTC | DOWN | 0.71 | 0.27 | -4.69 |
| 10-29 11:39 | +10 stop | DOGE | DOWN | 0.68 | 0.41 | -3.03 |
| 10-29 11:38 | +10 stop | DOGE | DOWN | 0.69 | 0.51 | -2.13 |
| 10-29 11:38 | +10 stop | ETH | UP | 0.58 | 0.81 | 2.01 |
| 10-29 11:38 | +10 | ETH | UP | 0.58 | 0.81 | 2.01 |
| 10-29 11:38 | +5 | ETH | UP | 0.58 | 0.81 | 2.01 |
| 10-29 11:38 | +10 stop | SOL | UP | 0.58 | 0.68 | 0.66 |
| 10-29 11:38 | +15 | SOL | UP | 0.59 | 0.78 | 1.60 |
| 10-29 11:38 | +10 | SOL | UP | 0.59 | 0.69 | 0.68 |
| 10-29 11:38 | +5 | SOL | UP | 0.59 | 0.68 | 0.57 |
| 10-29 11:37 | +5 | ZEC | UP | 0.71 | 0.76 | 0.25 |
| 10-29 11:37 | +10 stop | HYPE | UP | 0.62 | 0.75 | 0.98 |
| 10-29 11:37 | +10 stop | ZEC | UP | 0.62 | 0.76 | 1.10 |
| 10-29 11:37 | +20 | ZEC | UP | 0.62 | 0.83 | 1.83 |
| 10-29 11:37 | +15 | ZEC | UP | 0.62 | 0.77 | 1.20 |
| 10-29 11:37 | +10 | ZEC | UP | 0.62 | 0.76 | 1.10 |
| 10-29 11:37 | +5 | ZEC | UP | 0.60 | 0.65 | 0.17 |
| 10-29 11:37 | +10 stop | ETH | UP | 0.63 | 0.73 | 0.69 |
| 10-29 11:37 | +10 | ETH | UP | 0.63 | 0.73 | 0.69 |
| 10-29 11:37 | +5 | ETH | UP | 0.63 | 0.71 | 0.48 |
| 10-29 11:37 | +10 stop | BTC | DOWN | 0.68 | 0.81 | 1.03 |
| 10-29 11:37 | +5 | BTC | DOWN | 0.68 | 0.81 | 1.03 |
| 10-29 11:36 | +10 stop | DOGE | UP | 0.51 | 0.33 | -2.14 |
| 10-29 11:35 | +5 | BNB | DOWN | 0.57 | 0.67 | 0.65 |
| 10-29 11:35 | +10 stop | SOL | UP | 0.58 | 0.77 | 1.59 |
