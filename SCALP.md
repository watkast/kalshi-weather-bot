# Range-Scalp Bot

*Updated Thu Oct 29 08:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39008 | 34040 | 4968 (49) | 3 | $-10949.44 | -4.5% |
| **+10¢** | 29101 | 23368 | 5733 (71) | 5 | $-9663.64 | -5.3% |
| **+15¢** | 24340 | 18180 | 6160 (98) | 4 | $-8624.66 | -5.6% |
| **+20¢** | 21592 | 15136 | 6456 (127) | 4 | $-7543.45 | -5.6% |
| **+10¢ (15¢ stop)** | 47696 | 47629 | 67 (35) | 0 | $-18082.36 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 06:58 | +10 stop | BNB | DOWN | 0.66 | 0.76 | 0.71 |
| 10-29 06:58 | +5 | BNB | DOWN | 0.66 | 0.73 | 0.40 |
| 10-29 06:56 | +10 stop | XRP | DOWN | 0.39 | 0.55 | 1.25 |
| 10-29 06:55 | +10 stop | ZEC | UP | 0.70 | 0.82 | 0.94 |
| 10-29 06:55 | +5 | ZEC | UP | 0.69 | 0.82 | 1.04 |
| 10-29 06:54 | +10 stop | BNB | UP | 0.68 | 0.47 | -2.48 |
| 10-29 06:54 | +10 | BNB | UP | 0.69 | open |  |
| 10-29 06:54 | +5 | BNB | UP | 0.69 | 0.74 | 0.21 |
| 10-29 06:54 | +10 stop | XRP | DOWN | 0.60 | 0.43 | -2.05 |
| 10-29 06:54 | +10 stop | ZEC | UP | 0.56 | 0.67 | 0.76 |
| 10-29 06:54 | +5 | ZEC | UP | 0.56 | 0.67 | 0.76 |
| 10-29 06:53 | +10 stop | HYPE | DOWN | 0.55 | 0.39 | -1.95 |
| 10-29 06:52 | +10 stop | SOL | UP | 0.67 | 0.80 | 1.02 |
| 10-29 06:52 | +10 stop | BNB | UP | 0.63 | 0.74 | 0.79 |
| 10-29 06:52 | +10 | BNB | UP | 0.64 | 0.75 | 0.75 |
| 10-29 06:52 | +5 | BNB | UP | 0.65 | 0.74 | 0.60 |
| 10-29 06:52 | +10 stop | BNB | DOWN | 0.42 | 0.64 | 1.85 |
| 10-29 06:52 | +10 | BNB | DOWN | 0.42 | 0.64 | 1.85 |
| 10-29 06:52 | +5 | BNB | DOWN | 0.42 | 0.64 | 1.85 |
| 10-29 06:52 | +10 stop | SOL | DOWN | 0.51 | 0.36 | -1.85 |
| 10-29 06:52 | +10 stop | ZEC | DOWN | 0.63 | 0.46 | -2.05 |
| 10-29 06:52 | +15 | ZEC | DOWN | 0.63 | open |  |
| 10-29 06:52 | +10 | ZEC | DOWN | 0.63 | open |  |
| 10-29 06:52 | +5 | ZEC | DOWN | 0.63 | 0.68 | 0.17 |
| 10-29 06:51 | +15 | ETH | DOWN | 0.69 | 0.98 | 2.78 |
| 10-29 06:51 | +5 | ETH | DOWN | 0.69 | 0.77 | 0.52 |
| 10-29 06:51 | +10 stop | HYPE | DOWN | 0.68 | 0.53 | -1.87 |
| 10-29 06:51 | +15 | HYPE | DOWN | 0.68 | open |  |
| 10-29 06:51 | +10 | HYPE | DOWN | 0.68 | open |  |
| 10-29 06:51 | +5 | HYPE | DOWN | 0.68 | open |  |
| 10-29 06:50 | +5 | XRP | DOWN | 0.68 | open |  |
| 10-29 06:48 | +10 stop | ETH | DOWN | 0.69 | 0.54 | -1.83 |
| 10-29 06:48 | +10 | ETH | DOWN | 0.69 | 0.98 | 2.78 |
| 10-29 06:48 | +5 | ETH | DOWN | 0.69 | 0.74 | 0.21 |
| 10-29 06:48 | +10 stop | SOL | DOWN | 0.68 | 0.50 | -2.14 |
| 10-29 06:48 | +15 | SOL | DOWN | 0.69 | open |  |
| 10-29 06:48 | +10 | SOL | DOWN | 0.69 | open |  |
| 10-29 06:48 | +5 | SOL | DOWN | 0.69 | open |  |
| 10-29 06:47 | +10 stop | XRP | DOWN | 0.63 | 0.46 | -2.05 |
| 10-29 06:47 | +20 | XRP | DOWN | 0.63 | open |  |
