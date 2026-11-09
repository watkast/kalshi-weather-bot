# Range-Scalp Bot

*Updated Mon Nov 09 22:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53968 | 47070 | 6898 (89) | 1 | $-14752.09 | -4.3% |
| **+10¢** | 40307 | 32259 | 8048 (117) | 1 | $-13729.30 | -5.4% |
| **+15¢** | 33781 | 25107 | 8674 (149) | 2 | $-12503.31 | -5.9% |
| **+20¢** | 30071 | 20973 | 9098 (195) | 3 | $-10960.82 | -5.8% |
| **+10¢ (15¢ stop)** | 65741 | 65631 | 110 (66) | 0 | $-24345.35 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 22:28 | +10 stop | HYPE | DOWN | 0.61 | 0.91 | 2.75 |
| 11-09 22:28 | +20 | HYPE | DOWN | 0.59 | 0.91 | 2.95 |
| 11-09 22:28 | +15 | HYPE | DOWN | 0.60 | 0.91 | 2.85 |
| 11-09 22:28 | +10 | HYPE | DOWN | 0.60 | 0.91 | 2.85 |
| 11-09 22:28 | +5 | HYPE | DOWN | 0.61 | 0.91 | 2.75 |
| 11-09 22:27 | +10 stop | ETH | DOWN | 0.49 | 0.68 | 1.56 |
| 11-09 22:27 | +15 | ETH | DOWN | 0.49 | 0.68 | 1.56 |
| 11-09 22:27 | +10 | ETH | DOWN | 0.47 | 0.68 | 1.76 |
| 11-09 22:27 | +5 | ETH | DOWN | 0.47 | 0.68 | 1.76 |
| 11-09 22:27 | +10 stop | ZEC | UP | 0.62 | 0.91 | 2.68 |
| 11-09 22:27 | +10 | ZEC | UP | 0.62 | 0.91 | 2.68 |
| 11-09 22:27 | +5 | ZEC | UP | 0.62 | 0.91 | 2.68 |
| 11-09 22:26 | +5 | BTC | DOWN | 0.70 | 0.99 | 2.71 |
| 11-09 22:25 | +10 stop | BNB | UP | 0.57 | 0.83 | 2.32 |
| 11-09 22:24 | +10 stop | SOL | UP | 0.57 | 0.71 | 1.07 |
| 11-09 22:24 | +5 | BTC | DOWN | 0.59 | 0.65 | 0.27 |
| 11-09 22:24 | +10 stop | ETH | DOWN | 0.59 | 0.69 | 0.68 |
| 11-09 22:24 | +15 | ETH | DOWN | 0.59 | 0.77 | 1.50 |
| 11-09 22:24 | +10 | ETH | DOWN | 0.59 | 0.69 | 0.68 |
| 11-09 22:24 | +5 | ETH | DOWN | 0.59 | 0.69 | 0.68 |
| 11-09 22:22 | +10 stop | SOL | DOWN | 0.66 | 0.41 | -2.83 |
| 11-09 22:21 | +10 stop | NEAR | DOWN | 0.55 | 0.68 | 0.96 |
| 11-09 22:21 | +5 | BTC | DOWN | 0.61 | 0.68 | 0.37 |
| 11-09 22:20 | +10 stop | ZEC | DOWN | 0.67 | 0.45 | -2.54 |
| 11-09 22:20 | +10 stop | XRP | DOWN | 0.58 | 0.69 | 0.77 |
| 11-09 22:20 | +5 | BTC | DOWN | 0.66 | 0.73 | 0.40 |
| 11-09 22:19 | +5 | SOL | UP | 0.59 | 0.65 | 0.27 |
| 11-09 22:19 | +10 stop | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 11-09 22:19 | +20 | HYPE | DOWN | 0.62 | 0.82 | 1.72 |
| 11-09 22:19 | +15 | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 11-09 22:19 | +10 | HYPE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-09 22:19 | +5 | HYPE | DOWN | 0.62 | 0.68 | 0.27 |
| 11-09 22:19 | +10 stop | NEAR | UP | 0.57 | 0.41 | -1.95 |
| 11-09 22:19 | +5 | BTC | DOWN | 0.59 | 0.65 | 0.27 |
| 11-09 22:17 | +10 stop | DOGE | DOWN | 0.67 | 0.82 | 1.23 |
| 11-09 22:17 | +20 | DOGE | DOWN | 0.67 | 0.89 | 1.97 |
| 11-09 22:17 | +15 | DOGE | DOWN | 0.67 | 0.82 | 1.23 |
| 11-09 22:17 | +10 | DOGE | DOWN | 0.67 | 0.82 | 1.23 |
| 11-09 22:17 | +5 | DOGE | DOWN | 0.67 | 0.74 | 0.40 |
| 11-09 22:17 | +10 stop | BNB | DOWN | 0.69 | 0.52 | -1.99 |
