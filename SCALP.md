# Range-Scalp Bot

*Updated Sun Nov 01 10:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43468 | 37880 | 5588 (63) | 2 | $-12402.80 | -4.5% |
| **+10¢** | 32431 | 25978 | 6453 (85) | 2 | $-11093.51 | -5.4% |
| **+15¢** | 27142 | 20191 | 6951 (112) | 2 | $-10134.34 | -5.9% |
| **+20¢** | 24105 | 16825 | 7280 (146) | 2 | $-8929.84 | -5.9% |
| **+10¢ (15¢ stop)** | 53023 | 52938 | 85 (50) | 2 | $-20041.70 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 10:16 | +10 stop | BNB | DOWN | 0.58 | open |  |
| 11-01 10:16 | +20 | BNB | DOWN | 0.58 | open |  |
| 11-01 10:16 | +15 | BNB | DOWN | 0.58 | open |  |
| 11-01 10:16 | +10 | BNB | DOWN | 0.56 | open |  |
| 11-01 10:16 | +5 | BNB | DOWN | 0.57 | open |  |
| 11-01 10:16 | +10 stop | HYPE | DOWN | 0.55 | open |  |
| 11-01 10:16 | +20 | HYPE | DOWN | 0.55 | open |  |
| 11-01 10:16 | +15 | HYPE | DOWN | 0.55 | open |  |
| 11-01 10:16 | +10 | HYPE | DOWN | 0.55 | open |  |
| 11-01 10:16 | +5 | HYPE | DOWN | 0.55 | open |  |
| 11-01 10:12 | +10 stop | NEAR | UP | 0.71 | 0.86 | 1.27 |
| 11-01 10:12 | +20 | NEAR | UP | 0.71 | 0.92 | 1.90 |
| 11-01 10:12 | +15 | NEAR | UP | 0.71 | 0.86 | 1.27 |
| 11-01 10:12 | +10 | NEAR | UP | 0.71 | 0.86 | 1.27 |
| 11-01 10:12 | +5 | NEAR | UP | 0.71 | 0.86 | 1.27 |
| 11-01 10:10 | +10 stop | HYPE | UP | 0.65 | 0.75 | 0.70 |
| 11-01 10:10 | +10 | HYPE | UP | 0.65 | 0.75 | 0.70 |
| 11-01 10:10 | +5 | HYPE | UP | 0.65 | 0.75 | 0.70 |
| 11-01 10:10 | +10 stop | ZEC | UP | 0.48 | 0.29 | -2.23 |
| 11-01 10:09 | +10 | HYPE | UP | 0.62 | 0.74 | 0.85 |
| 11-01 10:09 | +5 | HYPE | UP | 0.62 | 0.74 | 0.85 |
| 11-01 10:08 | +10 stop | SOL | UP | 0.66 | 0.77 | 0.81 |
| 11-01 10:08 | +20 | SOL | UP | 0.66 | 0.89 | 2.07 |
| 11-01 10:08 | +15 | SOL | UP | 0.66 | 0.82 | 1.33 |
| 11-01 10:08 | +10 | SOL | UP | 0.66 | 0.77 | 0.81 |
| 11-01 10:08 | +5 | SOL | UP | 0.66 | 0.77 | 0.81 |
| 11-01 10:08 | +10 stop | ETH | UP | 0.69 | 0.83 | 1.15 |
| 11-01 10:08 | +10 | ETH | UP | 0.69 | 0.83 | 1.15 |
| 11-01 10:08 | +5 | ETH | UP | 0.69 | 0.83 | 1.15 |
| 11-01 10:08 | +10 stop | ZEC | DOWN | 0.59 | 0.44 | -1.85 |
| 11-01 10:08 | +20 | ZEC | DOWN | 0.59 | 0.82 | 2.02 |
| 11-01 10:08 | +15 | ZEC | DOWN | 0.59 | 0.82 | 2.02 |
| 11-01 10:08 | +10 | ZEC | DOWN | 0.59 | 0.69 | 0.68 |
| 11-01 10:08 | +5 | ZEC | DOWN | 0.59 | 0.69 | 0.68 |
| 11-01 10:07 | +10 stop | BNB | UP | 0.59 | 0.78 | 1.60 |
| 11-01 10:07 | +10 stop | BTC | DOWN | 0.67 | 0.30 | -4.01 |
| 11-01 10:07 | +5 | BTC | DOWN | 0.67 | yes | -6.86 |
| 11-01 10:07 | +10 stop | XRP | DOWN | 0.45 | 0.06 | -4.13 |
| 11-01 10:07 | +10 | XRP | DOWN | 0.45 | yes | -4.68 |
| 11-01 10:07 | +5 | XRP | DOWN | 0.45 | 0.53 | 0.44 |
