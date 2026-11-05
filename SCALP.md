# Range-Scalp Bot

*Updated Thu Nov 05 03:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47990 | 41794 | 6196 (73) | 4 | $-13797.96 | -4.6% |
| **+10¢** | 35846 | 28653 | 7193 (99) | 7 | $-12634.63 | -5.6% |
| **+15¢** | 30037 | 22293 | 7744 (127) | 7 | $-11543.25 | -6.1% |
| **+20¢** | 26683 | 18571 | 8112 (166) | 7 | $-10203.21 | -6.1% |
| **+10¢ (15¢ stop)** | 58501 | 58408 | 93 (56) | 0 | $-21732.07 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 03:40 | +10 stop | BNB | DOWN | 0.33 | 0.58 | 2.16 |
| 11-05 03:40 | +15 | BNB | DOWN | 0.32 | 0.58 | 2.26 |
| 11-05 03:40 | +5 | BNB | DOWN | 0.33 | 0.58 | 2.16 |
| 11-05 03:40 | +10 stop | BNB | DOWN | 0.58 | 0.69 | 0.77 |
| 11-05 03:39 | +10 stop | BTC | UP | 0.58 | 0.42 | -1.96 |
| 11-05 03:39 | +10 stop | BNB | UP | 0.46 | 0.66 | 1.66 |
| 11-05 03:39 | +10 stop | ETH | UP | 0.52 | 0.67 | 1.16 |
| 11-05 03:39 | +5 | ETH | UP | 0.52 | 0.67 | 1.16 |
| 11-05 03:38 | +10 stop | ZEC | UP | 0.62 | 0.39 | -2.64 |
| 11-05 03:37 | +10 stop | BNB | UP | 0.65 | 0.78 | 1.01 |
| 11-05 03:36 | +10 stop | BNB | UP | 0.57 | 0.75 | 1.48 |
| 11-05 03:36 | +10 stop | HYPE | DOWN | 0.60 | 0.26 | -3.71 |
| 11-05 03:36 | +20 | HYPE | DOWN | 0.60 | 0.86 | 2.34 |
| 11-05 03:36 | +10 | HYPE | DOWN | 0.60 | 0.74 | 1.09 |
| 11-05 03:36 | +5 | HYPE | DOWN | 0.60 | 0.74 | 1.09 |
| 11-05 03:35 | +10 stop | BTC | UP | 0.69 | 0.80 | 0.83 |
| 11-05 03:35 | +10 stop | ZEC | UP | 0.63 | 0.75 | 0.85 |
| 11-05 03:35 | +10 stop | DOGE | DOWN | 0.56 | 0.35 | -2.44 |
| 11-05 03:34 | +10 stop | BNB | DOWN | 0.60 | 0.42 | -2.20 |
| 11-05 03:34 | +10 | BNB | DOWN | 0.60 | 0.73 | 0.94 |
| 11-05 03:34 | +5 | BNB | DOWN | 0.62 | 0.69 | 0.38 |
| 11-05 03:33 | +10 stop | NEAR | UP | 0.61 | 0.76 | 1.20 |
| 11-05 03:33 | +10 stop | ETH | UP | 0.63 | 0.73 | 0.69 |
| 11-05 03:33 | +5 | XRP | UP | 0.65 | 0.77 | 0.90 |
| 11-05 03:33 | +5 | SOL | UP | 0.53 | 0.62 | 0.55 |
| 11-05 03:33 | +5 | ETH | UP | 0.62 | 0.67 | 0.17 |
| 11-05 03:33 | +10 stop | HYPE | DOWN | 0.59 | 0.70 | 0.78 |
| 11-05 03:33 | +10 | HYPE | DOWN | 0.57 | 0.68 | 0.76 |
| 11-05 03:33 | +15 | HYPE | DOWN | 0.61 | 0.78 | 1.40 |
| 11-05 03:33 | +5 | HYPE | DOWN | 0.63 | 0.68 | 0.17 |
| 11-05 03:33 | +10 stop | HYPE | DOWN | 0.58 | 0.69 | 0.77 |
| 11-05 03:33 | +10 | HYPE | DOWN | 0.58 | 0.69 | 0.77 |
| 11-05 03:33 | +10 stop | XRP | UP | 0.57 | 0.70 | 0.97 |
| 11-05 03:32 | +10 stop | ZEC | DOWN | 0.63 | 0.45 | -2.15 |
| 11-05 03:32 | +20 | ZEC | DOWN | 0.63 | open |  |
| 11-05 03:32 | +15 | ZEC | DOWN | 0.63 | open |  |
| 11-05 03:32 | +10 | ZEC | DOWN | 0.63 | open |  |
| 11-05 03:32 | +5 | ZEC | DOWN | 0.63 | open |  |
| 11-05 03:32 | +5 | XRP | UP | 0.59 | 0.66 | 0.37 |
| 11-05 03:32 | +10 stop | BNB | DOWN | 0.51 | 0.62 | 0.75 |
