# Range-Scalp Bot

*Updated Tue Nov 03 20:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46323 | 40338 | 5985 (72) | 5 | $-13310.67 | -4.6% |
| **+10¢** | 34580 | 27645 | 6935 (96) | 5 | $-12166.46 | -5.6% |
| **+15¢** | 28946 | 21486 | 7460 (124) | 6 | $-11124.53 | -6.1% |
| **+20¢** | 25713 | 17894 | 7819 (164) | 7 | $-9846.06 | -6.1% |
| **+10¢ (15¢ stop)** | 56502 | 56409 | 93 (56) | 1 | $-21179.95 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 20:52 | +10 stop | SOL | DOWN | 0.68 | 0.49 | -2.24 |
| 11-03 20:52 | +20 | SOL | DOWN | 0.67 | open |  |
| 11-03 20:52 | +15 | SOL | DOWN | 0.67 | open |  |
| 11-03 20:52 | +10 | SOL | DOWN | 0.67 | open |  |
| 11-03 20:52 | +5 | SOL | DOWN | 0.67 | open |  |
| 11-03 20:52 | +10 stop | BNB | UP | 0.59 | open |  |
| 11-03 20:50 | +10 stop | XRP | DOWN | 0.67 | 0.50 | -2.04 |
| 11-03 20:50 | +10 stop | BNB | DOWN | 0.70 | 0.54 | -1.93 |
| 11-03 20:50 | +10 stop | DOGE | UP | 0.55 | 0.68 | 0.96 |
| 11-03 20:50 | +20 | DOGE | UP | 0.55 | open |  |
| 11-03 20:50 | +15 | DOGE | UP | 0.55 | open |  |
| 11-03 20:50 | +10 | DOGE | UP | 0.55 | 0.68 | 0.96 |
| 11-03 20:50 | +5 | DOGE | UP | 0.55 | 0.64 | 0.55 |
| 11-03 20:49 | +10 stop | NEAR | DOWN | 0.68 | 0.82 | 1.13 |
| 11-03 20:49 | +10 | NEAR | DOWN | 0.70 | 0.82 | 0.94 |
| 11-03 20:48 | +5 | NEAR | DOWN | 0.70 | 0.75 | 0.21 |
| 11-03 20:48 | +10 stop | BNB | UP | 0.64 | 0.44 | -2.35 |
| 11-03 20:48 | +20 | BNB | UP | 0.64 | open |  |
| 11-03 20:48 | +15 | BNB | UP | 0.64 | open |  |
| 11-03 20:48 | +10 | BNB | UP | 0.64 | open |  |
| 11-03 20:48 | +5 | BNB | UP | 0.64 | open |  |
| 11-03 20:47 | +5 | XRP | UP | 0.61 | open |  |
| 11-03 20:47 | +10 stop | ETH | UP | 0.70 | 0.82 | 0.94 |
| 11-03 20:47 | +10 stop | SOL | UP | 0.67 | 0.33 | -3.72 |
| 11-03 20:47 | +10 stop | BTC | UP | 0.67 | 0.79 | 0.92 |
| 11-03 20:47 | +10 stop | XRP | UP | 0.59 | 0.43 | -1.95 |
| 11-03 20:47 | +20 | XRP | UP | 0.59 | open |  |
| 11-03 20:47 | +15 | XRP | UP | 0.58 | open |  |
| 11-03 20:47 | +10 | XRP | UP | 0.59 | open |  |
| 11-03 20:47 | +5 | XRP | UP | 0.60 | 0.65 | 0.17 |
| 11-03 20:46 | +10 stop | NEAR | DOWN | 0.56 | 0.69 | 0.97 |
| 11-03 20:46 | +20 | NEAR | DOWN | 0.55 | 0.75 | 1.68 |
| 11-03 20:46 | +15 | NEAR | DOWN | 0.55 | 0.75 | 1.68 |
| 11-03 20:46 | +10 | NEAR | DOWN | 0.55 | 0.69 | 1.07 |
| 11-03 20:46 | +5 | NEAR | DOWN | 0.55 | 0.61 | 0.25 |
| 11-03 20:46 | +10 stop | ETH | DOWN | 0.51 | 0.35 | -1.94 |
| 11-03 20:46 | +20 | ETH | DOWN | 0.51 | open |  |
| 11-03 20:46 | +15 | ETH | DOWN | 0.51 | open |  |
| 11-03 20:46 | +10 | ETH | DOWN | 0.51 | open |  |
| 11-03 20:46 | +5 | ETH | DOWN | 0.51 | open |  |
