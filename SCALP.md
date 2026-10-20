# Range-Scalp Bot

*Updated Tue Oct 20 14:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25769 | 22444 | 3325 (31) | 0 | $-7514.67 | -4.6% |
| **+10¢** | 19400 | 15560 | 3840 (46) | 0 | $-6626.12 | -5.4% |
| **+15¢** | 16241 | 12107 | 4134 (70) | 0 | $-5919.74 | -5.8% |
| **+20¢** | 14367 | 10038 | 4329 (88) | 2 | $-5285.00 | -5.9% |
| **+10¢ (15¢ stop)** | 31612 | 31559 | 53 (30) | 0 | $-11655.43 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 14:48 | +10 stop | ETH | DOWN | 0.67 | 0.77 | 0.71 |
| 10-20 14:48 | +10 | ETH | DOWN | 0.67 | 0.77 | 0.71 |
| 10-20 14:48 | +5 | ETH | DOWN | 0.67 | 0.77 | 0.71 |
| 10-20 14:48 | +5 | SOL | DOWN | 0.65 | 0.79 | 1.14 |
| 10-20 14:48 | +10 stop | XRP | DOWN | 0.63 | 0.76 | 1.00 |
| 10-20 14:48 | +10 | XRP | DOWN | 0.63 | 0.76 | 1.00 |
| 10-20 14:48 | +5 | XRP | DOWN | 0.63 | 0.76 | 1.00 |
| 10-20 14:46 | +10 stop | BNB | DOWN | 0.69 | 0.80 | 0.79 |
| 10-20 14:46 | +20 | BNB | DOWN | 0.69 | 0.90 | 1.84 |
| 10-20 14:46 | +15 | BNB | DOWN | 0.69 | 0.86 | 1.42 |
| 10-20 14:46 | +10 | BNB | DOWN | 0.69 | 0.80 | 0.79 |
| 10-20 14:46 | +5 | BNB | DOWN | 0.69 | 0.76 | 0.38 |
| 10-20 14:46 | +10 stop | BTC | DOWN | 0.71 | 0.84 | 1.05 |
| 10-20 14:46 | +20 | BTC | DOWN | 0.71 | 0.91 | 1.79 |
| 10-20 14:46 | +15 | BTC | DOWN | 0.71 | 0.87 | 1.37 |
| 10-20 14:46 | +10 | BTC | DOWN | 0.71 | 0.84 | 1.05 |
| 10-20 14:46 | +5 | BTC | DOWN | 0.71 | 0.79 | 0.53 |
| 10-20 14:46 | +10 stop | SOL | DOWN | 0.71 | 0.84 | 1.05 |
| 10-20 14:46 | +20 | SOL | DOWN | 0.71 | open |  |
| 10-20 14:46 | +15 | SOL | DOWN | 0.71 | 0.87 | 1.37 |
| 10-20 14:46 | +10 | SOL | DOWN | 0.70 | 0.84 | 1.15 |
| 10-20 14:46 | +5 | SOL | DOWN | 0.70 | 0.78 | 0.52 |
| 10-20 14:46 | +10 stop | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 10-20 14:46 | +20 | XRP | DOWN | 0.65 | open |  |
| 10-20 14:46 | +15 | XRP | DOWN | 0.65 | 0.82 | 1.43 |
| 10-20 14:46 | +10 | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 10-20 14:46 | +5 | XRP | DOWN | 0.66 | 0.75 | 0.60 |
| 10-20 14:45 | +10 stop | HYPE | DOWN | 0.58 | 0.75 | 1.38 |
| 10-20 14:45 | +20 | HYPE | DOWN | 0.58 | 0.80 | 1.90 |
| 10-20 14:45 | +15 | HYPE | DOWN | 0.58 | 0.75 | 1.38 |
| 10-20 14:45 | +10 | HYPE | DOWN | 0.58 | 0.75 | 1.38 |
| 10-20 14:45 | +5 | HYPE | DOWN | 0.58 | 0.63 | 0.15 |
| 10-20 14:45 | +10 stop | ETH | DOWN | 0.64 | 0.78 | 1.10 |
| 10-20 14:45 | +20 | ETH | DOWN | 0.64 | 0.84 | 1.73 |
| 10-20 14:45 | +15 | ETH | DOWN | 0.64 | 0.80 | 1.31 |
| 10-20 14:45 | +10 | ETH | DOWN | 0.64 | 0.78 | 1.10 |
| 10-20 14:45 | +5 | ETH | DOWN | 0.64 | 0.71 | 0.38 |
| 10-20 14:42 | +10 stop | SOL | UP | 0.59 | 0.16 | -4.57 |
| 10-20 14:42 | +20 | SOL | UP | 0.59 | no | -6.07 |
| 10-20 14:42 | +15 | SOL | UP | 0.59 | no | -6.07 |
