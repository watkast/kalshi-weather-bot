# Range-Scalp Bot

*Updated Wed Nov 04 08:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46968 | 40905 | 6063 (72) | 7 | $-13488.03 | -4.6% |
| **+10¢** | 35084 | 28054 | 7030 (96) | 8 | $-12300.46 | -5.6% |
| **+15¢** | 29377 | 21813 | 7564 (124) | 9 | $-11239.51 | -6.1% |
| **+20¢** | 26101 | 18177 | 7924 (164) | 9 | $-9901.28 | -6.0% |
| **+10¢ (15¢ stop)** | 57255 | 57162 | 93 (56) | 0 | $-21353.46 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 08:41 | +5 | NEAR | DOWN | 0.60 | 0.65 | 0.17 |
| 11-04 08:37 | +10 stop | XRP | UP | 0.68 | 0.80 | 0.92 |
| 11-04 08:37 | +10 | XRP | UP | 0.68 | 0.80 | 0.92 |
| 11-04 08:37 | +5 | XRP | UP | 0.68 | 0.80 | 0.92 |
| 11-04 08:37 | +10 stop | ZEC | UP | 0.66 | 0.76 | 0.71 |
| 11-04 08:37 | +10 stop | NEAR | DOWN | 0.68 | 0.48 | -2.34 |
| 11-04 08:35 | +10 stop | BNB | UP | 0.63 | 0.76 | 1.00 |
| 11-04 08:35 | +10 stop | ZEC | UP | 0.69 | 0.84 | 1.25 |
| 11-04 08:34 | +10 stop | DOGE | UP | 0.58 | 0.70 | 0.87 |
| 11-04 08:34 | +10 stop | NEAR | DOWN | 0.66 | 0.50 | -1.94 |
| 11-04 08:34 | +20 | NEAR | DOWN | 0.66 | open |  |
| 11-04 08:34 | +15 | NEAR | DOWN | 0.66 | open |  |
| 11-04 08:34 | +10 | NEAR | DOWN | 0.66 | open |  |
| 11-04 08:34 | +5 | NEAR | DOWN | 0.64 | 0.70 | 0.28 |
| 11-04 08:34 | +10 stop | SOL | UP | 0.69 | 0.81 | 0.94 |
| 11-04 08:33 | +10 stop | XRP | UP | 0.71 | 0.81 | 0.74 |
| 11-04 08:33 | +10 | XRP | UP | 0.71 | 0.81 | 0.74 |
| 11-04 08:33 | +5 | XRP | UP | 0.71 | 0.76 | 0.22 |
| 11-04 08:33 | +10 stop | BTC | UP | 0.71 | 0.83 | 0.95 |
| 11-04 08:33 | +10 stop | DOGE | DOWN | 0.54 | 0.38 | -1.95 |
| 11-04 08:33 | +20 | DOGE | DOWN | 0.56 | open |  |
| 11-04 08:33 | +15 | DOGE | DOWN | 0.56 | open |  |
| 11-04 08:33 | +10 | DOGE | DOWN | 0.56 | open |  |
| 11-04 08:33 | +5 | DOGE | DOWN | 0.56 | open |  |
| 11-04 08:33 | +10 stop | BNB | DOWN | 0.61 | 0.45 | -1.95 |
| 11-04 08:33 | +15 | BNB | DOWN | 0.61 | open |  |
| 11-04 08:33 | +10 | BNB | DOWN | 0.61 | open |  |
| 11-04 08:33 | +5 | BNB | DOWN | 0.61 | open |  |
| 11-04 08:32 | +10 stop | ZEC | DOWN | 0.53 | 0.36 | -2.05 |
| 11-04 08:32 | +5 | SOL | DOWN | 0.54 | open |  |
| 11-04 08:32 | +5 | HYPE | DOWN | 0.58 | open |  |
| 11-04 08:32 | +10 stop | SOL | DOWN | 0.54 | 0.36 | -2.15 |
| 11-04 08:32 | +10 | SOL | DOWN | 0.54 | open |  |
| 11-04 08:32 | +5 | SOL | DOWN | 0.53 | 0.62 | 0.55 |
| 11-04 08:32 | +5 | ETH | DOWN | 0.61 | open |  |
| 11-04 08:32 | +10 stop | ZEC | DOWN | 0.71 | 0.55 | -1.93 |
| 11-04 08:32 | +20 | ZEC | DOWN | 0.71 | open |  |
| 11-04 08:32 | +15 | ZEC | DOWN | 0.71 | open |  |
| 11-04 08:32 | +10 | ZEC | DOWN | 0.71 | open |  |
| 11-04 08:32 | +5 | ZEC | DOWN | 0.71 | open |  |
