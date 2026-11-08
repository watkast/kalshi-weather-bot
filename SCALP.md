# Range-Scalp Bot

*Updated Sun Nov 08 07:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 52147 | 45468 | 6679 (82) | 6 | $-14449.98 | -4.4% |
| **+10¢** | 38922 | 31136 | 7786 (107) | 7 | $-13444.15 | -5.5% |
| **+15¢** | 32596 | 24204 | 8392 (137) | 7 | $-12325.91 | -6.0% |
| **+20¢** | 28997 | 20200 | 8797 (181) | 9 | $-10857.06 | -6.0% |
| **+10¢ (15¢ stop)** | 63481 | 63376 | 105 (62) | 1 | $-23462.40 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 07:34 | +10 stop | DOGE | UP | 0.64 | open |  |
| 11-08 07:34 | +5 | DOGE | UP | 0.64 | 0.73 | 0.59 |
| 11-08 07:34 | +10 stop | ETH | UP | 0.67 | 0.77 | 0.71 |
| 11-08 07:33 | +10 stop | SOL | UP | 0.67 | 0.79 | 0.92 |
| 11-08 07:33 | +10 stop | HYPE | UP | 0.68 | 0.83 | 1.24 |
| 11-08 07:33 | +5 | ZEC | UP | 0.63 | 0.69 | 0.28 |
| 11-08 07:32 | +5 | DOGE | DOWN | 0.59 | 0.67 | 0.47 |
| 11-08 07:32 | +10 stop | BTC | UP | 0.56 | 0.74 | 1.48 |
| 11-08 07:32 | +10 stop | XRP | DOWN | 0.65 | 0.50 | -1.84 |
| 11-08 07:32 | +20 | XRP | DOWN | 0.64 | open |  |
| 11-08 07:32 | +15 | XRP | DOWN | 0.64 | open |  |
| 11-08 07:32 | +10 | XRP | DOWN | 0.64 | open |  |
| 11-08 07:32 | +5 | XRP | DOWN | 0.64 | open |  |
| 11-08 07:32 | +10 stop | NEAR | DOWN | 0.65 | 0.46 | -2.24 |
| 11-08 07:32 | +20 | NEAR | DOWN | 0.65 | open |  |
| 11-08 07:32 | +15 | NEAR | DOWN | 0.65 | open |  |
| 11-08 07:32 | +10 | NEAR | DOWN | 0.65 | open |  |
| 11-08 07:32 | +5 | NEAR | DOWN | 0.65 | open |  |
| 11-08 07:31 | +10 stop | HYPE | DOWN | 0.49 | 0.31 | -2.13 |
| 11-08 07:31 | +20 | HYPE | DOWN | 0.49 | open |  |
| 11-08 07:31 | +15 | HYPE | DOWN | 0.49 | open |  |
| 11-08 07:31 | +10 | HYPE | DOWN | 0.49 | open |  |
| 11-08 07:31 | +5 | HYPE | DOWN | 0.49 | open |  |
| 11-08 07:31 | +10 stop | ZEC | UP | 0.55 | 0.69 | 1.07 |
| 11-08 07:31 | +20 | ZEC | UP | 0.55 | open |  |
| 11-08 07:31 | +15 | ZEC | UP | 0.53 | 0.69 | 1.27 |
| 11-08 07:31 | +10 | ZEC | UP | 0.53 | 0.69 | 1.27 |
| 11-08 07:31 | +5 | ZEC | UP | 0.53 | 0.62 | 0.55 |
| 11-08 07:31 | +10 stop | DOGE | DOWN | 0.62 | 0.47 | -1.85 |
| 11-08 07:31 | +20 | DOGE | DOWN | 0.62 | open |  |
| 11-08 07:31 | +15 | DOGE | DOWN | 0.62 | open |  |
| 11-08 07:31 | +10 | DOGE | DOWN | 0.62 | open |  |
| 11-08 07:31 | +5 | DOGE | DOWN | 0.62 | 0.68 | 0.27 |
| 11-08 07:31 | +10 stop | SOL | DOWN | 0.58 | 0.41 | -2.05 |
| 11-08 07:31 | +20 | SOL | DOWN | 0.58 | open |  |
| 11-08 07:31 | +15 | SOL | DOWN | 0.58 | open |  |
| 11-08 07:31 | +10 | SOL | DOWN | 0.59 | open |  |
| 11-08 07:31 | +5 | SOL | DOWN | 0.60 | open |  |
| 11-08 07:31 | +10 stop | BTC | DOWN | 0.61 | 0.43 | -2.15 |
| 11-08 07:31 | +20 | BTC | DOWN | 0.61 | open |  |
