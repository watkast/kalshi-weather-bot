# Range-Scalp Bot

*Updated Fri Nov 13 19:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58511 | 51062 | 7449 (105) | 6 | $-15723.84 | -4.3% |
| **+10¢** | 43711 | 34999 | 8712 (139) | 8 | $-14686.33 | -5.3% |
| **+15¢** | 36634 | 27249 | 9385 (174) | 8 | $-13275.68 | -5.8% |
| **+20¢** | 32634 | 22781 | 9853 (225) | 8 | $-11655.93 | -5.7% |
| **+10¢ (15¢ stop)** | 71249 | 71115 | 134 (82) | 0 | $-26207.93 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 19:08 | +5 | BTC | UP | 0.58 | 0.64 | 0.25 |
| 11-13 19:07 | +10 stop | HYPE | UP | 0.68 | 0.85 | 1.45 |
| 11-13 19:07 | +10 stop | SOL | UP | 0.61 | 0.73 | 0.89 |
| 11-13 19:07 | +5 | XRP | DOWN | 0.70 | 0.79 | 0.63 |
| 11-13 19:07 | +10 stop | BTC | UP | 0.59 | 0.85 | 2.34 |
| 11-13 19:07 | +10 stop | DOGE | UP | 0.55 | 0.69 | 1.07 |
| 11-13 19:07 | +5 | BTC | UP | 0.61 | 0.68 | 0.37 |
| 11-13 19:07 | +10 stop | XRP | DOWN | 0.58 | 0.79 | 1.80 |
| 11-13 19:07 | +20 | XRP | DOWN | 0.58 | 0.79 | 1.80 |
| 11-13 19:07 | +15 | XRP | DOWN | 0.58 | 0.79 | 1.80 |
| 11-13 19:07 | +10 | XRP | DOWN | 0.58 | 0.79 | 1.80 |
| 11-13 19:07 | +5 | XRP | DOWN | 0.58 | 0.63 | 0.15 |
| 11-13 19:06 | +5 | BTC | DOWN | 0.53 | 0.62 | 0.55 |
| 11-13 19:06 | +10 stop | DOGE | DOWN | 0.60 | 0.43 | -2.05 |
| 11-13 19:06 | +10 | DOGE | DOWN | 0.60 | open |  |
| 11-13 19:06 | +10 stop | BNB | UP | 0.62 | 0.74 | 0.89 |
| 11-13 19:06 | +10 stop | NEAR | UP | 0.70 | 0.80 | 0.73 |
| 11-13 19:06 | +5 | DOGE | DOWN | 0.66 | open |  |
| 11-13 19:05 | +5 | BNB | UP | 0.71 | 0.77 | 0.32 |
| 11-13 19:05 | +5 | DOGE | DOWN | 0.51 | 0.56 | 0.14 |
| 11-13 19:05 | +5 | ETH | DOWN | 0.57 | open |  |
| 11-13 19:04 | +10 stop | SOL | DOWN | 0.63 | 0.47 | -1.95 |
| 11-13 19:04 | +10 | SOL | DOWN | 0.63 | open |  |
| 11-13 19:04 | +5 | SOL | DOWN | 0.63 | open |  |
| 11-13 19:04 | +10 stop | HYPE | DOWN | 0.60 | 0.40 | -2.37 |
| 11-13 19:04 | +20 | HYPE | DOWN | 0.60 | open |  |
| 11-13 19:04 | +15 | HYPE | DOWN | 0.60 | open |  |
| 11-13 19:04 | +10 | HYPE | DOWN | 0.60 | open |  |
| 11-13 19:04 | +5 | HYPE | DOWN | 0.60 | open |  |
| 11-13 19:04 | +10 stop | ETH | DOWN | 0.55 | 0.28 | -3.03 |
| 11-13 19:04 | +10 | ETH | DOWN | 0.55 | open |  |
| 11-13 19:04 | +5 | ETH | DOWN | 0.55 | 0.60 | 0.15 |
| 11-13 19:04 | +10 stop | BTC | DOWN | 0.69 | 0.40 | -3.22 |
| 11-13 19:04 | +20 | BTC | DOWN | 0.69 | open |  |
| 11-13 19:04 | +15 | BTC | DOWN | 0.69 | open |  |
| 11-13 19:04 | +10 | BTC | DOWN | 0.69 | open |  |
| 11-13 19:04 | +5 | BTC | DOWN | 0.69 | 0.77 | 0.52 |
| 11-13 19:04 | +10 stop | BNB | UP | 0.58 | 0.70 | 0.87 |
| 11-13 19:04 | +5 | BNB | UP | 0.58 | 0.64 | 0.25 |
| 11-13 19:03 | +10 stop | ETH | DOWN | 0.50 | 0.61 | 0.75 |
