# Range-Scalp Bot

*Updated Mon Nov 09 13:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53710 | 46844 | 6866 (86) | 5 | $-14733.65 | -4.4% |
| **+10¢** | 40120 | 32110 | 8010 (112) | 5 | $-13717.18 | -5.4% |
| **+15¢** | 33623 | 24992 | 8631 (143) | 5 | $-12489.42 | -5.9% |
| **+20¢** | 29923 | 20869 | 9054 (189) | 5 | $-10974.43 | -5.9% |
| **+10¢ (15¢ stop)** | 65441 | 65335 | 106 (63) | 3 | $-24222.93 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 13:26 | +5 | ZEC | DOWN | 0.60 | open |  |
| 11-09 13:25 | +10 stop | NEAR | DOWN | 0.68 | open |  |
| 11-09 13:24 | +10 stop | BNB | DOWN | 0.71 | open |  |
| 11-09 13:23 | +10 stop | ZEC | DOWN | 0.61 | open |  |
| 11-09 13:23 | +10 | ZEC | DOWN | 0.61 | open |  |
| 11-09 13:23 | +5 | ZEC | DOWN | 0.61 | 0.69 | 0.48 |
| 11-09 13:23 | +10 stop | SOL | DOWN | 0.61 | 0.72 | 0.78 |
| 11-09 13:23 | +15 | NEAR | UP | 0.69 | open |  |
| 11-09 13:23 | +5 | NEAR | UP | 0.69 | open |  |
| 11-09 13:22 | +10 stop | NEAR | UP | 0.64 | 0.47 | -2.05 |
| 11-09 13:21 | +10 stop | ZEC | UP | 0.64 | 0.46 | -2.15 |
| 11-09 13:21 | +15 | ZEC | UP | 0.60 | open |  |
| 11-09 13:21 | +10 | ZEC | UP | 0.60 | 0.70 | 0.70 |
| 11-09 13:21 | +5 | ZEC | UP | 0.60 | 0.70 | 0.70 |
| 11-09 13:21 | +10 stop | BNB | DOWN | 0.67 | 0.49 | -2.14 |
| 11-09 13:21 | +10 stop | SOL | DOWN | 0.69 | 0.51 | -2.13 |
| 11-09 13:21 | +10 stop | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-09 13:21 | +20 | DOGE | DOWN | 0.63 | 0.85 | 1.94 |
| 11-09 13:21 | +15 | DOGE | DOWN | 0.63 | 0.85 | 1.94 |
| 11-09 13:21 | +10 | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-09 13:21 | +5 | DOGE | DOWN | 0.63 | 0.69 | 0.28 |
| 11-09 13:20 | +10 stop | NEAR | UP | 0.60 | 0.70 | 0.68 |
| 11-09 13:20 | +10 stop | ETH | DOWN | 0.67 | 0.43 | -2.74 |
| 11-09 13:20 | +10 stop | BNB | DOWN | 0.68 | 0.51 | -2.04 |
| 11-09 13:19 | +5 | HYPE | DOWN | 0.61 | 0.77 | 1.30 |
| 11-09 13:19 | +10 stop | BNB | UP | 0.58 | 0.42 | -1.96 |
| 11-09 13:19 | +20 | BNB | UP | 0.56 | open |  |
| 11-09 13:19 | +15 | BNB | UP | 0.56 | open |  |
| 11-09 13:19 | +10 | BNB | UP | 0.56 | open |  |
| 11-09 13:19 | +5 | BNB | UP | 0.56 | open |  |
| 11-09 13:19 | +10 | DOGE | DOWN | 0.65 | 0.78 | 1.01 |
| 11-09 13:19 | +10 stop | HYPE | DOWN | 0.60 | 0.77 | 1.40 |
| 11-09 13:19 | +10 | HYPE | DOWN | 0.60 | 0.77 | 1.40 |
| 11-09 13:19 | +5 | HYPE | DOWN | 0.60 | 0.65 | 0.17 |
| 11-09 13:18 | +5 | DOGE | DOWN | 0.65 | 0.74 | 0.60 |
| 11-09 13:18 | +10 stop | NEAR | UP | 0.69 | 0.52 | -2.03 |
| 11-09 13:18 | +10 | NEAR | UP | 0.69 | open |  |
| 11-09 13:17 | +5 | BTC | DOWN | 0.62 | 0.67 | 0.17 |
| 11-09 13:17 | +5 | ZEC | UP | 0.67 | 0.76 | 0.61 |
| 11-09 13:17 | +5 | NEAR | UP | 0.68 | 0.73 | 0.25 |
