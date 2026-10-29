# Range-Scalp Bot

*Updated Thu Oct 29 12:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39249 | 34251 | 4998 (49) | 2 | $-11015.01 | -4.5% |
| **+10¢** | 29270 | 23501 | 5769 (71) | 3 | $-9738.73 | -5.3% |
| **+15¢** | 24472 | 18273 | 6199 (98) | 3 | $-8715.27 | -5.7% |
| **+20¢** | 21710 | 15216 | 6494 (127) | 3 | $-7608.20 | -5.6% |
| **+10¢ (15¢ stop)** | 47971 | 47904 | 67 (35) | 3 | $-18213.75 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 12:01 | +10 stop | BNB | UP | 0.51 | open |  |
| 10-29 12:01 | +20 | BNB | UP | 0.51 | open |  |
| 10-29 12:01 | +15 | BNB | UP | 0.51 | open |  |
| 10-29 12:01 | +10 | BNB | UP | 0.51 | open |  |
| 10-29 12:01 | +5 | BNB | UP | 0.51 | 0.57 | 0.24 |
| 10-29 12:01 | +10 stop | BTC | UP | 0.49 | open |  |
| 10-29 12:01 | +20 | BTC | UP | 0.49 | open |  |
| 10-29 12:01 | +15 | BTC | UP | 0.49 | open |  |
| 10-29 12:01 | +10 | BTC | UP | 0.49 | open |  |
| 10-29 12:01 | +5 | BTC | UP | 0.53 | open |  |
| 10-29 12:01 | +10 stop | DOGE | DOWN | 0.68 | open |  |
| 10-29 12:01 | +20 | DOGE | DOWN | 0.68 | open |  |
| 10-29 12:01 | +15 | DOGE | DOWN | 0.68 | open |  |
| 10-29 12:01 | +10 | DOGE | DOWN | 0.68 | open |  |
| 10-29 12:01 | +5 | DOGE | DOWN | 0.67 | open |  |
| 10-29 11:58 | +10 stop | DOGE | UP | 0.50 | 0.66 | 1.26 |
| 10-29 11:58 | +5 | DOGE | UP | 0.50 | 0.66 | 1.26 |
| 10-29 11:56 | +10 stop | DOGE | DOWN | 0.52 | 0.69 | 1.37 |
| 10-29 11:56 | +15 | DOGE | DOWN | 0.56 | 0.75 | 1.61 |
| 10-29 11:56 | +10 | DOGE | DOWN | 0.61 | 0.75 | 1.09 |
| 10-29 11:56 | +5 | DOGE | DOWN | 0.61 | 0.69 | 0.48 |
| 10-29 11:56 | +10 stop | NEAR | UP | 0.55 | 0.66 | 0.76 |
| 10-29 11:56 | +10 | NEAR | UP | 0.55 | 0.66 | 0.76 |
| 10-29 11:56 | +5 | NEAR | UP | 0.55 | 0.66 | 0.76 |
| 10-29 11:55 | +10 stop | BTC | UP | 0.29 | 0.55 | 2.27 |
| 10-29 11:54 | +10 stop | ETH | DOWN | 0.50 | 0.65 | 1.16 |
| 10-29 11:54 | +5 | NEAR | UP | 0.61 | 0.78 | 1.40 |
| 10-29 11:54 | +10 stop | BTC | UP | 0.52 | 0.35 | -2.04 |
| 10-29 11:54 | +5 | DOGE | DOWN | 0.65 | 0.70 | 0.19 |
| 10-29 11:53 | +5 | SOL | DOWN | 0.60 | 0.70 | 0.68 |
| 10-29 11:53 | +10 stop | DOGE | DOWN | 0.56 | 0.70 | 1.07 |
| 10-29 11:53 | +10 | DOGE | DOWN | 0.56 | 0.70 | 1.07 |
| 10-29 11:53 | +5 | DOGE | DOWN | 0.56 | 0.62 | 0.25 |
| 10-29 11:53 | +10 stop | NEAR | UP | 0.64 | 0.78 | 1.10 |
| 10-29 11:53 | +20 | NEAR | UP | 0.64 | no | -6.57 |
| 10-29 11:53 | +15 | NEAR | UP | 0.64 | no | -6.57 |
| 10-29 11:53 | +10 | NEAR | UP | 0.64 | 0.78 | 1.10 |
| 10-29 11:53 | +5 | NEAR | UP | 0.64 | 0.73 | 0.59 |
| 10-29 11:53 | +10 stop | BNB | UP | 0.65 | 0.95 | 2.79 |
| 10-29 11:53 | +20 | BNB | UP | 0.65 | 0.95 | 2.79 |
