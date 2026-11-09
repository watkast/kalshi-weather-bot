# Range-Scalp Bot

*Updated Mon Nov 09 07:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53510 | 46659 | 6851 (85) | 1 | $-14756.26 | -4.4% |
| **+10¢** | 39978 | 31988 | 7990 (110) | 1 | $-13743.80 | -5.5% |
| **+15¢** | 33497 | 24887 | 8610 (141) | 1 | $-12544.84 | -6.0% |
| **+20¢** | 29807 | 20777 | 9030 (186) | 1 | $-11043.22 | -5.9% |
| **+10¢ (15¢ stop)** | 65208 | 65102 | 106 (63) | 0 | $-24116.22 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 07:57 | +5 | ETH | DOWN | 0.55 | 0.69 | 1.07 |
| 11-09 07:56 | +10 stop | ETH | DOWN | 0.71 | 0.48 | -2.63 |
| 11-09 07:56 | +10 stop | ZEC | UP | 0.64 | 0.85 | 1.84 |
| 11-09 07:56 | +5 | SOL | DOWN | 0.70 | 0.77 | 0.42 |
| 11-09 07:55 | +10 stop | BNB | DOWN | 0.67 | 0.82 | 1.23 |
| 11-09 07:55 | +10 | BNB | DOWN | 0.65 | 0.82 | 1.43 |
| 11-09 07:55 | +5 | BNB | DOWN | 0.67 | 0.82 | 1.23 |
| 11-09 07:55 | +10 stop | ETH | UP | 0.60 | 0.36 | -2.74 |
| 11-09 07:54 | +10 stop | ZEC | DOWN | 0.54 | 0.32 | -2.54 |
| 11-09 07:54 | +10 stop | BTC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-09 07:54 | +10 stop | SOL | DOWN | 0.68 | 0.81 | 1.03 |
| 11-09 07:53 | +10 stop | ZEC | UP | 0.60 | 0.45 | -1.85 |
| 11-09 07:53 | +10 stop | XRP | DOWN | 0.71 | 0.81 | 0.75 |
| 11-09 07:51 | +10 | DOGE | DOWN | 0.70 | 0.86 | 1.36 |
| 11-09 07:51 | +10 stop | NEAR | DOWN | 0.65 | 0.78 | 1.01 |
| 11-09 07:51 | +20 | NEAR | DOWN | 0.65 | 0.86 | 1.85 |
| 11-09 07:51 | +15 | NEAR | DOWN | 0.66 | 0.83 | 1.44 |
| 11-09 07:51 | +10 | NEAR | DOWN | 0.66 | 0.78 | 0.91 |
| 11-09 07:51 | +5 | NEAR | DOWN | 0.65 | 0.72 | 0.39 |
| 11-09 07:51 | +10 stop | DOGE | DOWN | 0.60 | 0.75 | 1.19 |
| 11-09 07:51 | +5 | DOGE | DOWN | 0.60 | 0.67 | 0.37 |
| 11-09 07:51 | +10 stop | ETH | UP | 0.63 | 0.47 | -1.95 |
| 11-09 07:51 | +10 stop | SOL | UP | 0.63 | 0.46 | -2.05 |
| 11-09 07:50 | +10 stop | BNB | UP | 0.49 | 0.29 | -2.33 |
| 11-09 07:50 | +10 stop | BTC | UP | 0.54 | 0.37 | -2.05 |
| 11-09 07:50 | +5 | DOGE | UP | 0.55 | 0.64 | 0.55 |
| 11-09 07:50 | +10 stop | ETH | UP | 0.65 | 0.75 | 0.70 |
| 11-09 07:50 | +10 stop | SOL | UP | 0.61 | 0.73 | 0.89 |
| 11-09 07:49 | +10 stop | BNB | DOWN | 0.62 | 0.45 | -2.05 |
| 11-09 07:49 | +20 | BNB | DOWN | 0.62 | 0.82 | 1.72 |
| 11-09 07:49 | +15 | BNB | DOWN | 0.60 | 0.82 | 1.92 |
| 11-09 07:49 | +10 | BNB | DOWN | 0.59 | 0.69 | 0.68 |
| 11-09 07:49 | +5 | BNB | DOWN | 0.59 | 0.69 | 0.68 |
| 11-09 07:49 | +10 stop | XRP | UP | 0.57 | 0.37 | -2.35 |
| 11-09 07:49 | +10 stop | HYPE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-09 07:49 | +20 | HYPE | DOWN | 0.70 | 0.93 | 2.11 |
| 11-09 07:49 | +15 | HYPE | DOWN | 0.70 | 0.85 | 1.26 |
| 11-09 07:49 | +10 | HYPE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-09 07:49 | +5 | HYPE | DOWN | 0.70 | 0.78 | 0.52 |
| 11-09 07:49 | +10 stop | NEAR | DOWN | 0.54 | 0.70 | 1.27 |
