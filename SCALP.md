# Range-Scalp Bot

*Updated Mon Nov 09 02:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53200 | 46393 | 6807 (85) | 0 | $-14653.60 | -4.4% |
| **+10¢** | 39724 | 31784 | 7940 (110) | 0 | $-13646.88 | -5.5% |
| **+15¢** | 33286 | 24731 | 8555 (141) | 1 | $-12454.04 | -6.0% |
| **+20¢** | 29610 | 20640 | 8970 (186) | 1 | $-10954.49 | -5.9% |
| **+10¢ (15¢ stop)** | 64798 | 64692 | 106 (63) | 0 | $-24005.97 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 02:49 | +10 stop | NEAR | DOWN | 0.65 | 0.78 | 1.01 |
| 11-09 02:48 | +10 stop | NEAR | UP | 0.45 | 0.59 | 1.05 |
| 11-09 02:48 | +5 | BTC | DOWN | 0.62 | 0.74 | 0.89 |
| 11-09 02:47 | +10 stop | ZEC | DOWN | 0.62 | 0.78 | 1.30 |
| 11-09 02:47 | +20 | ZEC | DOWN | 0.61 | 0.82 | 1.82 |
| 11-09 02:47 | +15 | ZEC | DOWN | 0.61 | 0.78 | 1.40 |
| 11-09 02:47 | +10 | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 11-09 02:47 | +5 | ZEC | DOWN | 0.62 | 0.67 | 0.17 |
| 11-09 02:47 | +10 stop | BNB | DOWN | 0.62 | 0.79 | 1.41 |
| 11-09 02:47 | +20 | BNB | DOWN | 0.62 | 0.85 | 2.04 |
| 11-09 02:47 | +15 | BNB | DOWN | 0.62 | 0.79 | 1.41 |
| 11-09 02:47 | +10 | BNB | DOWN | 0.62 | 0.79 | 1.41 |
| 11-09 02:47 | +5 | BNB | DOWN | 0.62 | 0.79 | 1.41 |
| 11-09 02:47 | +10 stop | BTC | DOWN | 0.56 | 0.74 | 1.48 |
| 11-09 02:47 | +20 | BTC | DOWN | 0.56 | 0.77 | 1.79 |
| 11-09 02:47 | +15 | BTC | DOWN | 0.56 | 0.74 | 1.48 |
| 11-09 02:47 | +10 | BTC | DOWN | 0.56 | 0.74 | 1.48 |
| 11-09 02:47 | +5 | BTC | DOWN | 0.56 | 0.63 | 0.35 |
| 11-09 02:46 | +10 stop | XRP | DOWN | 0.67 | 0.82 | 1.23 |
| 11-09 02:46 | +20 | XRP | DOWN | 0.67 | 0.90 | 2.07 |
| 11-09 02:46 | +15 | XRP | DOWN | 0.67 | 0.82 | 1.23 |
| 11-09 02:46 | +10 | XRP | DOWN | 0.67 | 0.82 | 1.23 |
| 11-09 02:46 | +5 | XRP | DOWN | 0.67 | 0.72 | 0.19 |
| 11-09 02:46 | +10 stop | ETH | DOWN | 0.64 | 0.76 | 0.90 |
| 11-09 02:46 | +20 | ETH | DOWN | 0.64 | 0.89 | 2.26 |
| 11-09 02:46 | +15 | ETH | DOWN | 0.64 | 0.79 | 1.21 |
| 11-09 02:46 | +10 | ETH | DOWN | 0.64 | 0.76 | 0.90 |
| 11-09 02:46 | +5 | ETH | DOWN | 0.64 | 0.69 | 0.18 |
| 11-09 02:46 | +10 stop | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-09 02:46 | +10 | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-09 02:46 | +5 | DOGE | DOWN | 0.65 | 0.74 | 0.60 |
| 11-09 02:46 | +10 stop | SOL | DOWN | 0.65 | 0.77 | 0.91 |
| 11-09 02:46 | +20 | SOL | DOWN | 0.66 | 0.86 | 1.75 |
| 11-09 02:46 | +15 | SOL | DOWN | 0.66 | 0.83 | 1.44 |
| 11-09 02:46 | +10 | SOL | DOWN | 0.66 | 0.77 | 0.81 |
| 11-09 02:46 | +5 | SOL | DOWN | 0.66 | 0.72 | 0.29 |
| 11-09 02:46 | +10 stop | HYPE | DOWN | 0.63 | 0.79 | 1.30 |
| 11-09 02:46 | +20 | HYPE | DOWN | 0.63 | 0.85 | 1.93 |
| 11-09 02:46 | +15 | HYPE | DOWN | 0.63 | 0.79 | 1.31 |
| 11-09 02:46 | +10 | HYPE | DOWN | 0.63 | 0.73 | 0.69 |
