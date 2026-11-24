# Range-Scalp Bot

*Updated Tue Nov 24 21:48 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71132 | 62085 | 9047 (155) | 1 | $-18981.16 | -4.2% |
| **+10¢** | 53056 | 42486 | 10570 (201) | 3 | $-17610.46 | -5.3% |
| **+15¢** | 44438 | 33059 | 11379 (258) | 2 | $-15653.12 | -5.6% |
| **+20¢** | 39565 | 27585 | 11980 (324) | 3 | $-14033.02 | -5.7% |
| **+10¢ (15¢ stop)** | 86613 | 86412 | 201 (121) | 4 | $-31869.88 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 21:47 | +10 stop | SOL | UP | 0.64 | open |  |
| 11-24 21:47 | +10 | SOL | UP | 0.65 | open |  |
| 11-24 21:46 | +10 stop | BTC | UP | 0.68 | open |  |
| 11-24 21:46 | +20 | BTC | UP | 0.68 | open |  |
| 11-24 21:46 | +15 | BTC | UP | 0.68 | open |  |
| 11-24 21:46 | +10 | BTC | UP | 0.68 | open |  |
| 11-24 21:46 | +5 | BTC | UP | 0.68 | 0.75 | 0.40 |
| 11-24 21:46 | +5 | SOL | UP | 0.66 | 0.72 | 0.29 |
| 11-24 21:46 | +10 stop | NEAR | UP | 0.65 | 0.75 | 0.70 |
| 11-24 21:46 | +20 | NEAR | UP | 0.65 | open |  |
| 11-24 21:46 | +15 | NEAR | UP | 0.65 | 0.80 | 1.22 |
| 11-24 21:46 | +10 | NEAR | UP | 0.65 | 0.75 | 0.70 |
| 11-24 21:46 | +5 | NEAR | UP | 0.65 | 0.74 | 0.60 |
| 11-24 21:46 | +10 stop | DOGE | UP | 0.64 | open |  |
| 11-24 21:46 | +20 | DOGE | UP | 0.64 | open |  |
| 11-24 21:46 | +15 | DOGE | UP | 0.64 | open |  |
| 11-24 21:46 | +10 | DOGE | UP | 0.64 | open |  |
| 11-24 21:46 | +5 | DOGE | UP | 0.64 | open |  |
| 11-24 21:46 | +10 stop | ETH | UP | 0.67 | open |  |
| 11-24 21:46 | +5 | ETH | UP | 0.67 | 0.72 | 0.19 |
| 11-24 21:45 | +10 stop | SOL | UP | 0.49 | 0.61 | 0.85 |
| 11-24 21:45 | +20 | SOL | UP | 0.49 | 0.72 | 1.97 |
| 11-24 21:45 | +15 | SOL | UP | 0.49 | 0.67 | 1.46 |
| 11-24 21:45 | +10 | SOL | UP | 0.49 | 0.61 | 0.85 |
| 11-24 21:45 | +5 | SOL | UP | 0.48 | 0.55 | 0.34 |
| 11-24 21:45 | +10 stop | ETH | UP | 0.44 | 0.54 | 0.64 |
| 11-24 21:45 | +20 | ETH | UP | 0.45 | 0.72 | 2.37 |
| 11-24 21:45 | +15 | ETH | UP | 0.45 | 0.64 | 1.55 |
| 11-24 21:45 | +10 | ETH | UP | 0.45 | 0.55 | 0.64 |
| 11-24 21:45 | +5 | ETH | UP | 0.45 | 0.54 | 0.54 |
| 11-24 21:45 | +10 stop | ZEC | UP | 0.59 | 0.78 | 1.60 |
| 11-24 21:45 | +20 | ZEC | UP | 0.59 | 0.80 | 1.80 |
| 11-24 21:45 | +15 | ZEC | UP | 0.59 | 0.78 | 1.59 |
| 11-24 21:45 | +10 | ZEC | UP | 0.60 | 0.78 | 1.50 |
| 11-24 21:45 | +5 | ZEC | UP | 0.59 | 0.65 | 0.27 |
| 11-24 21:39 | +10 stop | NEAR | DOWN | 0.66 | 0.81 | 1.25 |
| 11-24 21:39 | +10 stop | BTC | DOWN | 0.63 | 0.86 | 2.04 |
| 11-24 21:39 | +10 stop | DOGE | DOWN | 0.58 | 0.70 | 0.87 |
| 11-24 21:38 | +10 stop | SOL | DOWN | 0.65 | 0.78 | 1.01 |
| 11-24 21:37 | +10 stop | NEAR | DOWN | 0.70 | 0.84 | 1.15 |
