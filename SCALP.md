# Range-Scalp Bot

*Updated Thu Nov 05 13:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48353 | 42128 | 6225 (73) | 4 | $-13785.17 | -4.5% |
| **+10¢** | 36099 | 28867 | 7232 (99) | 5 | $-12638.90 | -5.6% |
| **+15¢** | 30251 | 22464 | 7787 (127) | 5 | $-11524.10 | -6.1% |
| **+20¢** | 26875 | 18717 | 8158 (166) | 5 | $-10175.12 | -6.0% |
| **+10¢ (15¢ stop)** | 58939 | 58846 | 93 (56) | 0 | $-21891.95 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 13:58 | +10 stop | BNB | UP | 0.62 | 0.10 | -5.48 |
| 11-05 13:58 | +20 | BNB | UP | 0.62 | open |  |
| 11-05 13:58 | +15 | BNB | UP | 0.62 | open |  |
| 11-05 13:58 | +10 | BNB | UP | 0.62 | open |  |
| 11-05 13:58 | +5 | BNB | UP | 0.62 | 0.70 | 0.48 |
| 11-05 13:57 | +10 stop | BTC | DOWN | 0.54 | 0.68 | 1.06 |
| 11-05 13:57 | +10 stop | DOGE | DOWN | 0.59 | 0.81 | 1.92 |
| 11-05 13:56 | +10 stop | BTC | UP | 0.71 | 0.44 | -3.03 |
| 11-05 13:56 | +10 | BTC | UP | 0.71 | open |  |
| 11-05 13:56 | +5 | BTC | UP | 0.71 | open |  |
| 11-05 13:55 | +5 | ZEC | UP | 0.64 | open |  |
| 11-05 13:55 | +10 stop | DOGE | UP | 0.70 | 0.49 | -2.39 |
| 11-05 13:55 | +10 stop | ZEC | UP | 0.66 | 0.46 | -2.34 |
| 11-05 13:55 | +10 stop | SOL | UP | 0.63 | 0.73 | 0.69 |
| 11-05 13:55 | +5 | SOL | UP | 0.63 | 0.73 | 0.69 |
| 11-05 13:53 | +10 stop | DOGE | DOWN | 0.64 | 0.47 | -2.05 |
| 11-05 13:53 | +5 | SOL | DOWN | 0.52 | 0.59 | 0.35 |
| 11-05 13:53 | +10 stop | BTC | UP | 0.64 | 0.77 | 1.00 |
| 11-05 13:53 | +20 | BTC | UP | 0.64 | open |  |
| 11-05 13:53 | +15 | BTC | UP | 0.64 | open |  |
| 11-05 13:53 | +10 | BTC | UP | 0.64 | 0.77 | 1.00 |
| 11-05 13:53 | +5 | BTC | UP | 0.64 | 0.77 | 1.00 |
| 11-05 13:53 | +10 stop | ZEC | DOWN | 0.66 | 0.45 | -2.44 |
| 11-05 13:52 | +10 stop | XRP | UP | 0.57 | 0.69 | 0.87 |
| 11-05 13:52 | +5 | XRP | UP | 0.56 | 0.61 | 0.15 |
| 11-05 13:52 | +10 stop | SOL | DOWN | 0.68 | 0.44 | -2.74 |
| 11-05 13:52 | +20 | SOL | DOWN | 0.68 | 0.97 | 2.69 |
| 11-05 13:52 | +15 | SOL | DOWN | 0.68 | 0.84 | 1.34 |
| 11-05 13:52 | +10 | SOL | DOWN | 0.68 | 0.81 | 1.03 |
| 11-05 13:52 | +5 | SOL | DOWN | 0.68 | 0.75 | 0.40 |
| 11-05 13:51 | +10 stop | BNB | UP | 0.70 | 0.80 | 0.73 |
| 11-05 13:51 | +20 | BNB | UP | 0.70 | 0.91 | 1.85 |
| 11-05 13:51 | +15 | BNB | UP | 0.70 | 0.91 | 1.85 |
| 11-05 13:51 | +10 | BNB | UP | 0.70 | 0.80 | 0.73 |
| 11-05 13:51 | +5 | BNB | UP | 0.70 | 0.76 | 0.32 |
| 11-05 13:51 | +10 stop | NEAR | UP | 0.64 | 0.49 | -1.85 |
| 11-05 13:51 | +20 | NEAR | UP | 0.64 | 0.85 | 1.84 |
| 11-05 13:51 | +15 | NEAR | UP | 0.64 | 0.85 | 1.84 |
| 11-05 13:51 | +10 | NEAR | UP | 0.64 | 0.74 | 0.69 |
| 11-05 13:51 | +5 | NEAR | UP | 0.64 | 0.71 | 0.38 |
