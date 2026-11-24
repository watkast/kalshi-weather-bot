# Range-Scalp Bot

*Updated Tue Nov 24 05:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70444 | 61485 | 8959 (148) | 0 | $-18836.42 | -4.2% |
| **+10¢** | 52558 | 42096 | 10462 (192) | 0 | $-17451.54 | -5.3% |
| **+15¢** | 44030 | 32761 | 11269 (248) | 0 | $-15541.26 | -5.6% |
| **+20¢** | 39208 | 27344 | 11864 (314) | 0 | $-13908.95 | -5.7% |
| **+10¢ (15¢ stop)** | 85777 | 85579 | 198 (118) | 0 | $-31537.68 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 05:02 | +10 stop | ZEC | UP | 0.68 | 0.78 | 0.71 |
| 11-24 05:02 | +20 | ZEC | UP | 0.67 | 0.89 | 1.97 |
| 11-24 05:02 | +15 | ZEC | UP | 0.67 | 0.82 | 1.23 |
| 11-24 05:02 | +10 | ZEC | UP | 0.68 | 0.78 | 0.71 |
| 11-24 05:02 | +5 | ZEC | UP | 0.68 | 0.75 | 0.40 |
| 11-24 02:08 | +10 | ETH | UP | 0.59 | yes | 3.93 |
| 11-24 02:08 | +5 | ETH | UP | 0.59 | 0.64 | 0.16 |
| 11-24 02:08 | +10 stop | HYPE | DOWN | 0.59 | 0.69 | 0.68 |
| 11-24 02:08 | +20 | HYPE | DOWN | 0.60 | no | 3.85 |
| 11-24 02:08 | +15 | HYPE | DOWN | 0.59 | no | 3.94 |
| 11-24 02:08 | +10 | HYPE | DOWN | 0.58 | 0.69 | 0.77 |
| 11-24 02:08 | +5 | HYPE | DOWN | 0.58 | 0.69 | 0.77 |
| 11-24 02:07 | +10 stop | XRP | UP | 0.68 | no | -6.96 |
| 11-24 02:07 | +10 stop | BNB | DOWN | 0.49 | 0.63 | 1.07 |
| 11-24 02:07 | +20 | BNB | DOWN | 0.46 | no | 5.21 |
| 11-24 02:07 | +15 | BNB | DOWN | 0.46 | 0.63 | 1.35 |
| 11-24 02:07 | +10 | BNB | DOWN | 0.47 | 0.63 | 1.25 |
| 11-24 02:07 | +5 | BNB | DOWN | 0.49 | 0.63 | 1.07 |
| 11-24 02:07 | +10 stop | ETH | DOWN | 0.45 | yes | -4.68 |
| 11-24 02:07 | +20 | ETH | DOWN | 0.42 | yes | -4.38 |
| 11-24 02:07 | +15 | ETH | DOWN | 0.41 | yes | -4.27 |
| 11-24 02:07 | +10 | ETH | DOWN | 0.41 | 0.53 | 0.85 |
| 11-24 02:07 | +5 | ETH | DOWN | 0.41 | 0.53 | 0.85 |
| 11-24 02:06 | +10 stop | DOGE | UP | 0.49 | 0.61 | 0.85 |
| 11-24 02:06 | +10 stop | XRP | UP | 0.39 | 0.52 | 0.95 |
| 11-24 02:05 | +10 stop | SOL | DOWN | 0.65 | 0.41 | -2.73 |
| 11-24 02:05 | +20 | SOL | DOWN | 0.65 | yes | -6.66 |
| 11-24 02:05 | +15 | SOL | DOWN | 0.65 | yes | -6.66 |
| 11-24 02:05 | +10 | SOL | DOWN | 0.65 | yes | -6.66 |
| 11-24 02:05 | +5 | SOL | DOWN | 0.66 | yes | -6.76 |
| 11-24 02:05 | +10 stop | DOGE | DOWN | 0.53 | 0.31 | -2.53 |
| 11-24 02:05 | +20 | DOGE | DOWN | 0.53 | yes | -5.48 |
| 11-24 02:05 | +15 | DOGE | DOWN | 0.53 | yes | -5.48 |
| 11-24 02:05 | +10 | DOGE | DOWN | 0.53 | yes | -5.48 |
| 11-24 02:05 | +5 | DOGE | DOWN | 0.53 | yes | -5.48 |
| 11-24 02:05 | +10 stop | NEAR | DOWN | 0.55 | 0.69 | 1.07 |
| 11-24 02:05 | +5 | NEAR | DOWN | 0.55 | 0.69 | 1.07 |
| 11-24 02:05 | +10 stop | XRP | DOWN | 0.62 | 0.43 | -2.25 |
| 11-24 02:05 | +20 | XRP | DOWN | 0.62 | no | 3.63 |
| 11-24 02:05 | +15 | XRP | DOWN | 0.62 | no | 3.63 |
