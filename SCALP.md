# Range-Scalp Bot

*Updated Mon Nov 09 03:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53251 | 46431 | 6820 (85) | 0 | $-14711.13 | -4.4% |
| **+10¢** | 39770 | 31815 | 7955 (110) | 0 | $-13709.24 | -5.5% |
| **+15¢** | 33324 | 24753 | 8571 (141) | 0 | $-12519.02 | -6.0% |
| **+20¢** | 29645 | 20658 | 8987 (186) | 0 | $-11023.89 | -5.9% |
| **+10¢ (15¢ stop)** | 64879 | 64773 | 106 (63) | 0 | $-24067.42 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 03:46 | +10 stop | HYPE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-09 03:46 | +20 | HYPE | DOWN | 0.64 | 0.86 | 1.94 |
| 11-09 03:46 | +15 | HYPE | DOWN | 0.64 | 0.81 | 1.42 |
| 11-09 03:46 | +10 | HYPE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-09 03:46 | +5 | HYPE | DOWN | 0.65 | 0.70 | 0.19 |
| 11-09 03:46 | +10 stop | ZEC | DOWN | 0.65 | 0.77 | 0.91 |
| 11-09 03:46 | +20 | ZEC | DOWN | 0.65 | 0.86 | 1.85 |
| 11-09 03:46 | +15 | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 11-09 03:46 | +10 | ZEC | DOWN | 0.65 | 0.77 | 0.91 |
| 11-09 03:46 | +5 | ZEC | DOWN | 0.65 | 0.77 | 0.91 |
| 11-09 03:45 | +10 stop | BNB | DOWN | 0.70 | 0.83 | 1.05 |
| 11-09 03:45 | +20 | BNB | DOWN | 0.70 | 0.90 | 1.78 |
| 11-09 03:45 | +10 stop | NEAR | DOWN | 0.66 | 0.77 | 0.81 |
| 11-09 03:45 | +20 | NEAR | DOWN | 0.66 | 0.87 | 1.86 |
| 11-09 03:45 | +15 | NEAR | DOWN | 0.66 | 0.84 | 1.54 |
| 11-09 03:45 | +10 | NEAR | DOWN | 0.66 | 0.77 | 0.81 |
| 11-09 03:45 | +5 | NEAR | DOWN | 0.66 | 0.77 | 0.81 |
| 11-09 03:45 | +10 stop | XRP | DOWN | 0.70 | 0.83 | 1.05 |
| 11-09 03:45 | +20 | XRP | DOWN | 0.70 | 0.94 | 2.26 |
| 11-09 03:45 | +15 | XRP | DOWN | 0.71 | 0.86 | 1.26 |
| 11-09 03:45 | +10 | XRP | DOWN | 0.71 | 0.83 | 0.95 |
| 11-09 03:45 | +5 | XRP | DOWN | 0.71 | 0.83 | 0.95 |
| 11-09 03:45 | +15 | BNB | DOWN | 0.71 | 0.89 | 1.58 |
| 11-09 03:45 | +10 | BNB | DOWN | 0.71 | 0.83 | 0.95 |
| 11-09 03:45 | +5 | BNB | DOWN | 0.71 | 0.76 | 0.22 |
| 11-09 03:45 | +10 stop | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 11-09 03:45 | +20 | ETH | DOWN | 0.70 | 0.91 | 1.89 |
| 11-09 03:45 | +15 | ETH | DOWN | 0.70 | 0.85 | 1.26 |
| 11-09 03:45 | +10 | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 11-09 03:45 | +5 | ETH | DOWN | 0.70 | 0.76 | 0.32 |
| 11-09 03:41 | +10 stop | SOL | DOWN | 0.69 | 0.24 | -4.78 |
| 11-09 03:41 | +10 stop | BTC | DOWN | 0.59 | 0.42 | -2.05 |
| 11-09 03:40 | +10 stop | ZEC | DOWN | 0.58 | 0.31 | -3.03 |
| 11-09 03:38 | +10 stop | BNB | DOWN | 0.70 | 0.52 | -2.13 |
| 11-09 03:38 | +10 stop | ZEC | UP | 0.62 | 0.46 | -1.95 |
| 11-09 03:38 | +20 | ZEC | UP | 0.62 | 0.88 | 2.35 |
| 11-09 03:38 | +15 | ZEC | UP | 0.62 | 0.79 | 1.41 |
| 11-09 03:38 | +10 | ZEC | UP | 0.62 | 0.79 | 1.41 |
| 11-09 03:38 | +5 | ZEC | UP | 0.62 | 0.68 | 0.27 |
| 11-09 03:38 | +10 stop | SOL | DOWN | 0.69 | 0.80 | 0.83 |
