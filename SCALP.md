# Range-Scalp Bot

*Updated Wed Nov 11 22:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56270 | 49071 | 7199 (95) | 0 | $-15383.72 | -4.3% |
| **+10¢** | 42049 | 33647 | 8402 (125) | 0 | $-14359.08 | -5.4% |
| **+15¢** | 35261 | 26207 | 9054 (159) | 0 | $-13038.19 | -5.9% |
| **+20¢** | 31414 | 21914 | 9500 (209) | 0 | $-11395.58 | -5.8% |
| **+10¢ (15¢ stop)** | 68580 | 68459 | 121 (73) | 0 | $-25292.92 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 21:57 | +10 stop | ZEC | DOWN | 0.61 | 0.72 | 0.83 |
| 11-11 21:57 | +5 | ZEC | DOWN | 0.60 | 0.72 | 0.88 |
| 11-11 21:55 | +10 stop | ZEC | UP | 0.41 | 0.57 | 1.25 |
| 11-11 21:55 | +5 | ZEC | UP | 0.44 | 0.57 | 0.94 |
| 11-11 21:54 | +10 stop | NEAR | DOWN | 0.67 | 0.86 | 1.65 |
| 11-11 21:53 | +10 stop | ZEC | UP | 0.55 | 0.66 | 0.72 |
| 11-11 21:53 | +5 | ZEC | UP | 0.55 | 0.66 | 0.72 |
| 11-11 21:53 | +10 stop | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-11 21:52 | +10 stop | ZEC | UP | 0.68 | 0.52 | -1.92 |
| 11-11 21:52 | +10 stop | DOGE | UP | 0.53 | 0.63 | 0.68 |
| 11-11 21:52 | +10 stop | HYPE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-11 21:51 | +5 | ETH | DOWN | 0.62 | 0.68 | 0.27 |
| 11-11 21:51 | +10 stop | NEAR | DOWN | 0.67 | 0.49 | -2.14 |
| 11-11 21:48 | +10 stop | NEAR | DOWN | 0.51 | 0.62 | 0.75 |
| 11-11 21:48 | +10 stop | DOGE | DOWN | 0.60 | 0.45 | -1.85 |
| 11-11 21:47 | +10 stop | SOL | DOWN | 0.59 | 0.72 | 0.98 |
| 11-11 21:47 | +10 stop | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 11-11 21:47 | +5 | ETH | DOWN | 0.59 | 0.65 | 0.27 |
| 11-11 21:47 | +10 stop | BTC | DOWN | 0.61 | 0.73 | 0.89 |
| 11-11 21:47 | +10 stop | NEAR | DOWN | 0.70 | 0.52 | -2.13 |
| 11-11 21:47 | +10 stop | ZEC | DOWN | 0.60 | 0.41 | -2.24 |
| 11-11 21:47 | +10 stop | HYPE | DOWN | 0.65 | 0.79 | 1.12 |
| 11-11 21:47 | +10 stop | BNB | DOWN | 0.70 | 0.81 | 0.84 |
| 11-11 21:47 | +20 | BNB | DOWN | 0.70 | 0.95 | 2.34 |
| 11-11 21:47 | +15 | BNB | DOWN | 0.70 | 0.87 | 1.47 |
| 11-11 21:47 | +10 | BNB | DOWN | 0.70 | 0.81 | 0.84 |
| 11-11 21:47 | +5 | BNB | DOWN | 0.70 | 0.75 | 0.22 |
| 11-11 21:46 | +10 stop | ETH | UP | 0.61 | 0.72 | 0.73 |
| 11-11 21:46 | +20 | ETH | UP | 0.63 | no | -6.49 |
| 11-11 21:46 | +15 | ETH | UP | 0.63 | no | -6.49 |
| 11-11 21:46 | +10 | ETH | UP | 0.63 | no | -6.49 |
| 11-11 21:46 | +5 | ETH | UP | 0.63 | 0.72 | 0.56 |
| 11-11 21:46 | +10 stop | ZEC | UP | 0.65 | 0.48 | -2.04 |
| 11-11 21:46 | +20 | ZEC | UP | 0.65 | no | -6.66 |
| 11-11 21:46 | +15 | ZEC | UP | 0.65 | no | -6.66 |
| 11-11 21:46 | +10 | ZEC | UP | 0.65 | no | -6.66 |
| 11-11 21:46 | +5 | ZEC | UP | 0.65 | 0.70 | 0.19 |
| 11-11 21:46 | +10 stop | HYPE | UP | 0.64 | 0.43 | -2.45 |
| 11-11 21:46 | +20 | HYPE | UP | 0.64 | no | -6.57 |
| 11-11 21:46 | +15 | HYPE | UP | 0.64 | no | -6.57 |
