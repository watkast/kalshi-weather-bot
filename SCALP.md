# Range-Scalp Bot

*Updated Tue Nov 10 01:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54114 | 47206 | 6908 (89) | 0 | $-14731.83 | -4.3% |
| **+10¢** | 40421 | 32359 | 8062 (117) | 0 | $-13694.56 | -5.4% |
| **+15¢** | 33880 | 25191 | 8689 (149) | 0 | $-12456.90 | -5.9% |
| **+20¢** | 30167 | 21054 | 9113 (195) | 0 | $-10874.79 | -5.8% |
| **+10¢ (15¢ stop)** | 65920 | 65810 | 110 (66) | 0 | $-24403.70 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 01:06 | +10 stop | DOGE | UP | 0.68 | 0.85 | 1.45 |
| 11-10 01:06 | +20 | DOGE | UP | 0.68 | 0.89 | 1.87 |
| 11-10 01:06 | +15 | DOGE | UP | 0.68 | 0.85 | 1.45 |
| 11-10 01:06 | +10 | DOGE | UP | 0.68 | 0.85 | 1.45 |
| 11-10 01:06 | +5 | DOGE | UP | 0.68 | 0.73 | 0.20 |
| 11-10 01:04 | +10 stop | ZEC | UP | 0.61 | 0.71 | 0.68 |
| 11-10 01:04 | +20 | ZEC | UP | 0.61 | 0.83 | 1.93 |
| 11-10 01:04 | +15 | ZEC | UP | 0.61 | 0.76 | 1.20 |
| 11-10 01:04 | +10 | ZEC | UP | 0.61 | 0.71 | 0.68 |
| 11-10 01:04 | +5 | ZEC | UP | 0.62 | 0.68 | 0.27 |
| 11-10 01:00 | +10 stop | NEAR | UP | 0.65 | 0.77 | 0.91 |
| 11-10 01:00 | +20 | NEAR | UP | 0.65 | 0.85 | 1.75 |
| 11-10 01:00 | +15 | NEAR | UP | 0.65 | 0.82 | 1.43 |
| 11-10 01:00 | +10 | NEAR | UP | 0.65 | 0.77 | 0.91 |
| 11-10 01:00 | +5 | NEAR | UP | 0.65 | 0.77 | 0.91 |
| 11-10 00:56 | +10 stop | NEAR | DOWN | 0.68 | 0.86 | 1.55 |
| 11-10 00:56 | +10 stop | NEAR | UP | 0.56 | 0.41 | -1.85 |
| 11-10 00:55 | +10 stop | ZEC | UP | 0.61 | 0.26 | -3.81 |
| 11-10 00:54 | +10 stop | XRP | UP | 0.53 | 0.36 | -2.05 |
| 11-10 00:54 | +5 | XRP | UP | 0.53 | 0.81 | 2.51 |
| 11-10 00:54 | +10 stop | DOGE | DOWN | 0.67 | 0.85 | 1.55 |
| 11-10 00:54 | +20 | DOGE | DOWN | 0.67 | 0.92 | 2.27 |
| 11-10 00:54 | +15 | DOGE | DOWN | 0.67 | 0.85 | 1.55 |
| 11-10 00:54 | +10 | DOGE | DOWN | 0.67 | 0.85 | 1.55 |
| 11-10 00:54 | +5 | DOGE | DOWN | 0.67 | 0.76 | 0.61 |
| 11-10 00:53 | +10 stop | NEAR | DOWN | 0.65 | 0.40 | -2.83 |
| 11-10 00:53 | +20 | NEAR | DOWN | 0.65 | 0.86 | 1.85 |
| 11-10 00:53 | +15 | NEAR | DOWN | 0.65 | 0.86 | 1.85 |
| 11-10 00:53 | +10 | NEAR | DOWN | 0.65 | 0.86 | 1.85 |
| 11-10 00:53 | +5 | NEAR | DOWN | 0.65 | 0.86 | 1.85 |
| 11-10 00:52 | +10 stop | HYPE | DOWN | 0.64 | 0.45 | -2.25 |
| 11-10 00:52 | +5 | BNB | DOWN | 0.71 | 0.76 | 0.22 |
| 11-10 00:52 | +5 | ZEC | DOWN | 0.58 | 0.73 | 1.18 |
| 11-10 00:51 | +10 | BNB | DOWN | 0.70 | 0.80 | 0.73 |
| 11-10 00:51 | +10 stop | XRP | DOWN | 0.66 | 0.36 | -3.33 |
| 11-10 00:51 | +10 stop | BNB | DOWN | 0.66 | 0.76 | 0.71 |
| 11-10 00:51 | +10 stop | ZEC | DOWN | 0.71 | 0.48 | -2.63 |
| 11-10 00:50 | +5 | XRP | UP | 0.54 | 0.63 | 0.55 |
| 11-10 00:50 | +10 stop | SOL | DOWN | 0.60 | 0.77 | 1.40 |
| 11-10 00:49 | +10 stop | ETH | UP | 0.54 | 0.34 | -2.34 |
