# Range-Scalp Bot

*Updated Sat Oct 31 07:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41962 | 36612 | 5350 (54) | 2 | $-11789.02 | -4.5% |
| **+10¢** | 31282 | 25087 | 6195 (78) | 2 | $-10556.37 | -5.4% |
| **+15¢** | 26151 | 19472 | 6679 (106) | 2 | $-9647.59 | -5.9% |
| **+20¢** | 23223 | 16229 | 6994 (137) | 2 | $-8494.21 | -5.8% |
| **+10¢ (15¢ stop)** | 51153 | 51078 | 75 (41) | 0 | $-19284.29 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 07:33 | +10 stop | ZEC | DOWN | 0.71 | 0.84 | 1.08 |
| 10-31 07:33 | +10 stop | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-31 07:33 | +5 | HYPE | DOWN | 0.64 | 0.78 | 1.10 |
| 10-31 07:32 | +10 stop | HYPE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-31 07:32 | +20 | HYPE | DOWN | 0.59 | 0.85 | 2.34 |
| 10-31 07:32 | +15 | HYPE | DOWN | 0.59 | 0.78 | 1.60 |
| 10-31 07:32 | +10 | HYPE | DOWN | 0.59 | 0.78 | 1.60 |
| 10-31 07:32 | +5 | HYPE | DOWN | 0.59 | 0.64 | 0.16 |
| 10-31 07:32 | +10 stop | ZEC | UP | 0.45 | 0.25 | -2.32 |
| 10-31 07:32 | +20 | ZEC | UP | 0.45 | open |  |
| 10-31 07:32 | +15 | ZEC | UP | 0.45 | open |  |
| 10-31 07:32 | +10 | ZEC | UP | 0.45 | open |  |
| 10-31 07:32 | +5 | ZEC | UP | 0.45 | open |  |
| 10-31 07:32 | +10 stop | ETH | UP | 0.52 | 0.34 | -2.14 |
| 10-31 07:32 | +20 | ETH | UP | 0.52 | open |  |
| 10-31 07:32 | +15 | ETH | UP | 0.52 | open |  |
| 10-31 07:32 | +10 | ETH | UP | 0.52 | open |  |
| 10-31 07:32 | +5 | ETH | UP | 0.52 | open |  |
| 10-31 07:32 | +10 stop | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 10-31 07:32 | +20 | BNB | DOWN | 0.64 | 0.85 | 1.84 |
| 10-31 07:32 | +15 | BNB | DOWN | 0.64 | 0.83 | 1.68 |
| 10-31 07:32 | +10 | BNB | DOWN | 0.64 | 0.74 | 0.74 |
| 10-31 07:32 | +5 | BNB | DOWN | 0.64 | 0.71 | 0.43 |
| 10-31 07:32 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-31 07:32 | +20 | BTC | DOWN | 0.66 | 0.88 | 1.96 |
| 10-31 07:32 | +15 | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 10-31 07:32 | +10 | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-31 07:32 | +5 | BTC | DOWN | 0.66 | 0.74 | 0.50 |
| 10-31 07:31 | +10 stop | ZEC | DOWN | 0.36 | 0.57 | 1.75 |
| 10-31 07:31 | +20 | ZEC | DOWN | 0.36 | 0.57 | 1.75 |
| 10-31 07:31 | +15 | ZEC | DOWN | 0.36 | 0.57 | 1.75 |
| 10-31 07:31 | +10 | ZEC | DOWN | 0.36 | 0.57 | 1.75 |
| 10-31 07:31 | +5 | ZEC | DOWN | 0.36 | 0.57 | 1.75 |
| 10-31 07:31 | +10 stop | SOL | DOWN | 0.59 | 0.72 | 0.98 |
| 10-31 07:31 | +20 | SOL | DOWN | 0.60 | 0.81 | 1.82 |
| 10-31 07:31 | +15 | SOL | DOWN | 0.59 | 0.81 | 1.91 |
| 10-31 07:31 | +10 | SOL | DOWN | 0.61 | 0.72 | 0.78 |
| 10-31 07:31 | +5 | SOL | DOWN | 0.61 | 0.72 | 0.78 |
| 10-31 07:31 | +10 stop | XRP | DOWN | 0.69 | 0.82 | 1.04 |
| 10-31 07:31 | +20 | XRP | DOWN | 0.69 | 0.94 | 2.25 |
