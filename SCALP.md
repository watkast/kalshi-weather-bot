# Range-Scalp Bot

*Updated Mon Nov 23 10:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69835 | 60936 | 8899 (146) | 0 | $-18807.01 | -4.3% |
| **+10¢** | 52112 | 41714 | 10398 (189) | 0 | $-17504.13 | -5.3% |
| **+15¢** | 43671 | 32470 | 11201 (245) | 1 | $-15631.25 | -5.7% |
| **+20¢** | 38888 | 27103 | 11785 (310) | 1 | $-13982.64 | -5.7% |
| **+10¢ (15¢ stop)** | 85055 | 84865 | 190 (118) | 0 | $-31247.24 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 10:46 | +10 stop | SOL | UP | 0.71 | 0.82 | 0.84 |
| 11-23 10:46 | +20 | SOL | UP | 0.71 | 0.93 | 1.99 |
| 11-23 10:46 | +15 | SOL | UP | 0.71 | 0.86 | 1.26 |
| 11-23 10:46 | +10 | SOL | UP | 0.71 | 0.82 | 0.84 |
| 11-23 10:46 | +5 | SOL | UP | 0.71 | 0.77 | 0.32 |
| 11-23 10:46 | +10 stop | NEAR | UP | 0.69 | 0.80 | 0.83 |
| 11-23 10:46 | +20 | NEAR | UP | 0.69 | open |  |
| 11-23 10:46 | +15 | NEAR | UP | 0.70 | open |  |
| 11-23 10:46 | +10 | NEAR | UP | 0.70 | 0.80 | 0.73 |
| 11-23 10:46 | +5 | NEAR | UP | 0.70 | 0.75 | 0.21 |
| 11-23 10:41 | +10 stop | BTC | UP | 0.67 | 0.47 | -2.34 |
| 11-23 10:41 | +20 | BTC | UP | 0.67 | no | -6.86 |
| 11-23 10:41 | +15 | BTC | UP | 0.67 | no | -6.86 |
| 11-23 10:41 | +10 | BTC | UP | 0.67 | no | -6.86 |
| 11-23 10:41 | +5 | BTC | UP | 0.67 | 0.72 | 0.19 |
| 11-23 10:41 | +10 stop | ETH | DOWN | 0.67 | 0.49 | -2.14 |
| 11-23 10:41 | +5 | ETH | DOWN | 0.67 | 0.74 | 0.40 |
| 11-23 10:41 | +10 stop | ZEC | DOWN | 0.71 | 0.85 | 1.16 |
| 11-23 10:41 | +5 | ZEC | DOWN | 0.70 | 0.85 | 1.22 |
| 11-23 10:40 | +10 stop | NEAR | UP | 0.62 | 0.80 | 1.51 |
| 11-23 10:40 | +10 | NEAR | UP | 0.62 | 0.80 | 1.51 |
| 11-23 10:40 | +5 | NEAR | UP | 0.62 | 0.80 | 1.51 |
| 11-23 10:39 | +10 stop | BNB | DOWN | 0.57 | 0.72 | 1.17 |
| 11-23 10:39 | +10 stop | NEAR | UP | 0.55 | 0.67 | 0.86 |
| 11-23 10:39 | +10 | NEAR | UP | 0.55 | 0.67 | 0.86 |
| 11-23 10:39 | +5 | NEAR | UP | 0.55 | 0.67 | 0.86 |
| 11-23 10:39 | +10 stop | SOL | UP | 0.69 | 0.50 | -2.23 |
| 11-23 10:39 | +10 | SOL | UP | 0.69 | 0.83 | 1.15 |
| 11-23 10:39 | +5 | SOL | UP | 0.69 | 0.83 | 1.15 |
| 11-23 10:39 | +10 stop | ZEC | DOWN | 0.51 | 0.64 | 0.95 |
| 11-23 10:39 | +5 | ZEC | DOWN | 0.51 | 0.59 | 0.45 |
| 11-23 10:38 | +10 stop | BNB | UP | 0.64 | 0.44 | -2.35 |
| 11-23 10:37 | +10 stop | ETH | UP | 0.56 | 0.34 | -2.54 |
| 11-23 10:36 | +10 stop | BNB | UP | 0.48 | 0.65 | 1.36 |
| 11-23 10:36 | +10 stop | NEAR | DOWN | 0.34 | 0.64 | 2.67 |
| 11-23 10:35 | +10 stop | SOL | UP | 0.65 | 0.75 | 0.70 |
| 11-23 10:35 | +10 | SOL | UP | 0.65 | 0.75 | 0.70 |
| 11-23 10:35 | +5 | SOL | UP | 0.65 | 0.75 | 0.70 |
| 11-23 10:35 | +10 stop | ZEC | DOWN | 0.64 | 0.49 | -1.85 |
| 11-23 10:35 | +20 | ZEC | DOWN | 0.64 | 0.85 | 1.84 |
