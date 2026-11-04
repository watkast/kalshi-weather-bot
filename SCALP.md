# Range-Scalp Bot

*Updated Wed Nov 04 02:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46693 | 40662 | 6031 (72) | 2 | $-13404.75 | -4.6% |
| **+10¢** | 34879 | 27888 | 6991 (96) | 2 | $-12230.52 | -5.6% |
| **+15¢** | 29208 | 21687 | 7521 (124) | 2 | $-11173.12 | -6.1% |
| **+20¢** | 25945 | 18068 | 7877 (164) | 2 | $-9829.94 | -6.0% |
| **+10¢ (15¢ stop)** | 56930 | 56837 | 93 (56) | 2 | $-21259.20 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 02:45 | +10 stop | XRP | DOWN | 0.61 | open |  |
| 11-04 02:45 | +20 | XRP | DOWN | 0.61 | open |  |
| 11-04 02:45 | +15 | XRP | DOWN | 0.61 | open |  |
| 11-04 02:45 | +10 | XRP | DOWN | 0.61 | open |  |
| 11-04 02:45 | +5 | XRP | DOWN | 0.61 | open |  |
| 11-04 02:45 | +10 stop | NEAR | DOWN | 0.56 | open |  |
| 11-04 02:45 | +20 | NEAR | DOWN | 0.56 | open |  |
| 11-04 02:45 | +15 | NEAR | DOWN | 0.56 | open |  |
| 11-04 02:45 | +10 | NEAR | DOWN | 0.56 | open |  |
| 11-04 02:45 | +5 | NEAR | DOWN | 0.56 | open |  |
| 11-04 02:42 | +10 stop | XRP | DOWN | 0.55 | 0.72 | 1.37 |
| 11-04 02:42 | +20 | XRP | DOWN | 0.55 | yes | -5.68 |
| 11-04 02:42 | +15 | XRP | DOWN | 0.54 | 0.72 | 1.47 |
| 11-04 02:42 | +10 | XRP | DOWN | 0.54 | 0.64 | 0.65 |
| 11-04 02:42 | +5 | XRP | DOWN | 0.54 | 0.64 | 0.65 |
| 11-04 02:40 | +10 stop | HYPE | UP | 0.58 | 0.68 | 0.66 |
| 11-04 02:39 | +10 stop | HYPE | DOWN | 0.62 | 0.43 | -2.25 |
| 11-04 02:39 | +5 | HYPE | DOWN | 0.62 | yes | -6.37 |
| 11-04 02:37 | +10 stop | SOL | DOWN | 0.66 | 0.76 | 0.71 |
| 11-04 02:37 | +10 stop | XRP | DOWN | 0.62 | 0.79 | 1.41 |
| 11-04 02:37 | +10 stop | BNB | DOWN | 0.70 | 0.84 | 1.15 |
| 11-04 02:37 | +10 | BNB | DOWN | 0.70 | 0.84 | 1.15 |
| 11-04 02:36 | +5 | BNB | DOWN | 0.65 | 0.71 | 0.25 |
| 11-04 02:36 | +10 stop | DOGE | DOWN | 0.62 | 0.74 | 0.89 |
| 11-04 02:35 | +10 stop | SOL | DOWN | 0.48 | 0.61 | 0.95 |
| 11-04 02:35 | +10 stop | BNB | DOWN | 0.52 | 0.63 | 0.75 |
| 11-04 02:35 | +10 | BNB | DOWN | 0.52 | 0.63 | 0.75 |
| 11-04 02:35 | +5 | BNB | DOWN | 0.52 | 0.60 | 0.45 |
| 11-04 02:35 | +10 stop | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 11-04 02:35 | +10 stop | BNB | UP | 0.48 | 0.58 | 0.64 |
| 11-04 02:35 | +20 | BNB | UP | 0.48 | no | -4.98 |
| 11-04 02:35 | +15 | BNB | UP | 0.48 | no | -4.98 |
| 11-04 02:35 | +10 | BNB | UP | 0.48 | 0.58 | 0.64 |
| 11-04 02:35 | +5 | BNB | UP | 0.49 | 0.58 | 0.54 |
| 11-04 02:34 | +10 stop | HYPE | UP | 0.66 | 0.30 | -3.90 |
| 11-04 02:34 | +10 stop | ZEC | DOWN | 0.63 | 0.73 | 0.69 |
| 11-04 02:34 | +10 | ZEC | DOWN | 0.63 | 0.73 | 0.69 |
| 11-04 02:34 | +5 | ZEC | DOWN | 0.64 | 0.71 | 0.38 |
| 11-04 02:33 | +10 stop | BTC | DOWN | 0.66 | 0.51 | -1.84 |
| 11-04 02:33 | +5 | SOL | DOWN | 0.64 | 0.69 | 0.18 |
