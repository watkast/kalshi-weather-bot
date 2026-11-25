# Range-Scalp Bot

*Updated Wed Nov 25 07:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71599 | 62499 | 9100 (157) | 0 | $-19036.64 | -4.2% |
| **+10¢** | 53405 | 42774 | 10631 (203) | 0 | $-17656.72 | -5.3% |
| **+15¢** | 44729 | 33284 | 11445 (260) | 0 | $-15687.13 | -5.6% |
| **+20¢** | 39825 | 27770 | 12055 (326) | 0 | $-14095.43 | -5.6% |
| **+10¢ (15¢ stop)** | 87170 | 86967 | 203 (123) | 0 | $-32032.49 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-25 07:16 | +10 stop | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 11-25 07:16 | +20 | ETH | DOWN | 0.70 | 0.91 | 1.87 |
| 11-25 07:16 | +15 | ETH | DOWN | 0.70 | 0.88 | 1.57 |
| 11-25 07:16 | +10 | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 11-25 07:16 | +5 | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 11-25 07:16 | +5 | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 11-25 07:16 | +10 stop | DOGE | DOWN | 0.70 | 0.81 | 0.85 |
| 11-25 07:16 | +20 | DOGE | DOWN | 0.69 | 0.91 | 2.00 |
| 11-25 07:16 | +15 | DOGE | DOWN | 0.69 | 0.84 | 1.25 |
| 11-25 07:16 | +10 | DOGE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-25 07:16 | +5 | DOGE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-25 07:16 | +5 | HYPE | DOWN | 0.71 | 0.77 | 0.32 |
| 11-25 07:16 | +10 stop | SOL | DOWN | 0.71 | 0.84 | 1.05 |
| 11-25 07:16 | +20 | SOL | DOWN | 0.71 | 0.95 | 2.24 |
| 11-25 07:16 | +15 | SOL | DOWN | 0.71 | 0.87 | 1.37 |
| 11-25 07:16 | +10 | SOL | DOWN | 0.71 | 0.84 | 1.05 |
| 11-25 07:16 | +5 | SOL | DOWN | 0.71 | 0.79 | 0.53 |
| 11-25 07:11 | +10 stop | ZEC | UP | 0.64 | 0.85 | 1.84 |
| 11-25 07:09 | +10 stop | DOGE | DOWN | 0.51 | 0.67 | 1.26 |
| 11-25 07:08 | +10 stop | ZEC | UP | 0.56 | 0.66 | 0.66 |
| 11-25 07:07 | +10 stop | NEAR | DOWN | 0.64 | 0.74 | 0.69 |
| 11-25 07:07 | +15 | NEAR | DOWN | 0.65 | 0.84 | 1.64 |
| 11-25 07:07 | +10 | NEAR | DOWN | 0.65 | 0.78 | 1.01 |
| 11-25 07:07 | +5 | NEAR | DOWN | 0.65 | 0.74 | 0.60 |
| 11-25 07:05 | +10 stop | ZEC | UP | 0.70 | 0.51 | -2.23 |
| 11-25 07:05 | +10 stop | NEAR | DOWN | 0.57 | 0.69 | 0.87 |
| 11-25 07:05 | +10 | NEAR | DOWN | 0.57 | 0.69 | 0.87 |
| 11-25 07:05 | +5 | NEAR | DOWN | 0.57 | 0.64 | 0.35 |
| 11-25 07:04 | +5 | ZEC | DOWN | 0.55 | 0.77 | 1.89 |
| 11-25 07:04 | +10 stop | XRP | UP | 0.57 | 0.67 | 0.66 |
| 11-25 07:04 | +10 stop | BTC | DOWN | 0.56 | 0.40 | -1.95 |
| 11-25 07:04 | +10 stop | HYPE | DOWN | 0.59 | 0.35 | -2.73 |
| 11-25 07:03 | +10 stop | XRP | UP | 0.54 | 0.64 | 0.65 |
| 11-25 07:02 | +5 | ETH | DOWN | 0.68 | yes | -6.96 |
| 11-25 07:02 | +10 stop | DOGE | DOWN | 0.67 | 0.46 | -2.44 |
| 11-25 07:02 | +20 | DOGE | DOWN | 0.67 | 0.89 | 1.97 |
| 11-25 07:02 | +15 | DOGE | DOWN | 0.67 | 0.82 | 1.23 |
| 11-25 07:02 | +10 | DOGE | DOWN | 0.67 | 0.82 | 1.23 |
| 11-25 07:02 | +5 | DOGE | DOWN | 0.67 | 0.82 | 1.23 |
| 11-25 07:02 | +5 | SOL | DOWN | 0.63 | yes | -6.47 |
