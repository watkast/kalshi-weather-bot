# Range-Scalp Bot

*Updated Thu Nov 05 04:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48050 | 41847 | 6203 (73) | 5 | $-13814.29 | -4.6% |
| **+10¢** | 35892 | 28688 | 7204 (99) | 8 | $-12665.52 | -5.6% |
| **+15¢** | 30075 | 22319 | 7756 (127) | 7 | $-11573.16 | -6.1% |
| **+20¢** | 26715 | 18590 | 8125 (166) | 8 | $-10240.87 | -6.1% |
| **+10¢ (15¢ stop)** | 58577 | 58484 | 93 (56) | 0 | $-21769.16 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 04:57 | +10 stop | NEAR | UP | 0.61 | 0.34 | -3.03 |
| 11-05 04:57 | +10 | NEAR | UP | 0.61 | open |  |
| 11-05 04:57 | +5 | NEAR | UP | 0.61 | 0.66 | 0.17 |
| 11-05 04:57 | +10 stop | HYPE | DOWN | 0.63 | 0.47 | -1.96 |
| 11-05 04:57 | +10 | HYPE | DOWN | 0.63 | open |  |
| 11-05 04:57 | +5 | HYPE | DOWN | 0.63 | open |  |
| 11-05 04:56 | +10 stop | HYPE | DOWN | 0.47 | 0.58 | 0.74 |
| 11-05 04:56 | +10 | HYPE | DOWN | 0.48 | 0.58 | 0.64 |
| 11-05 04:56 | +5 | HYPE | DOWN | 0.48 | 0.58 | 0.64 |
| 11-05 04:54 | +10 stop | NEAR | DOWN | 0.65 | 0.40 | -2.83 |
| 11-05 04:52 | +10 stop | NEAR | DOWN | 0.61 | 0.72 | 0.78 |
| 11-05 04:52 | +10 stop | ZEC | DOWN | 0.69 | 0.85 | 1.36 |
| 11-05 04:51 | +10 stop | HYPE | DOWN | 0.69 | 0.84 | 1.25 |
| 11-05 04:51 | +10 | HYPE | DOWN | 0.69 | 0.84 | 1.25 |
| 11-05 04:51 | +5 | HYPE | DOWN | 0.69 | 0.84 | 1.25 |
| 11-05 04:51 | +5 | ZEC | DOWN | 0.65 | 0.73 | 0.50 |
| 11-05 04:51 | +10 stop | HYPE | UP | 0.57 | 0.67 | 0.66 |
| 11-05 04:51 | +15 | HYPE | UP | 0.57 | 0.81 | 2.11 |
| 11-05 04:51 | +10 | HYPE | UP | 0.57 | 0.67 | 0.66 |
| 11-05 04:51 | +5 | HYPE | UP | 0.57 | 0.67 | 0.66 |
| 11-05 04:50 | +10 stop | ZEC | UP | 0.53 | 0.36 | -2.05 |
| 11-05 04:50 | +15 | ZEC | UP | 0.53 | open |  |
| 11-05 04:50 | +10 | ZEC | UP | 0.53 | open |  |
| 11-05 04:50 | +5 | ZEC | UP | 0.54 | 0.60 | 0.25 |
| 11-05 04:50 | +10 stop | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 11-05 04:49 | +10 stop | BNB | DOWN | 0.57 | 0.71 | 1.02 |
| 11-05 04:49 | +5 | BTC | DOWN | 0.69 | 0.76 | 0.42 |
| 11-05 04:49 | +5 | ETH | DOWN | 0.66 | 0.75 | 0.60 |
| 11-05 04:49 | +10 stop | BNB | DOWN | 0.53 | 0.64 | 0.75 |
| 11-05 04:49 | +5 | BTC | DOWN | 0.62 | 0.69 | 0.38 |
| 11-05 04:48 | +10 stop | NEAR | DOWN | 0.53 | 0.38 | -1.85 |
| 11-05 04:48 | +10 stop | DOGE | DOWN | 0.66 | 0.80 | 1.12 |
| 11-05 04:47 | +10 stop | ZEC | DOWN | 0.65 | 0.31 | -3.71 |
| 11-05 04:47 | +10 stop | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 11-05 04:47 | +10 stop | HYPE | UP | 0.67 | 0.78 | 0.81 |
| 11-05 04:47 | +20 | HYPE | UP | 0.67 | open |  |
| 11-05 04:47 | +15 | HYPE | UP | 0.67 | 0.83 | 1.34 |
| 11-05 04:47 | +10 | HYPE | UP | 0.67 | 0.78 | 0.81 |
| 11-05 04:47 | +5 | HYPE | UP | 0.67 | 0.72 | 0.19 |
| 11-05 04:47 | +10 stop | BTC | DOWN | 0.67 | 0.79 | 0.92 |
